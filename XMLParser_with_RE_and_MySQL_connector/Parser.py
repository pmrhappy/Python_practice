import xml.etree.ElementTree as etree
import re,os,io
import configparser
from collections import OrderedDict
import collections
from mysql import connector
import csv

# INSERT mode: create whole mfc_config table 
# (^only for a new project to customize DB)

# UPDATE mode: update the existed components

mode="UPDATE"   #  "INSERT" or "UPDATE" 
component_name="UserName"
config_file_name="config.ini"

CSV_Output=True
Database_write_back=False

#------------------ Patterns for Search (in Regular Expression)
Q_group_pattern="(Q\d+)"

device_pattern="A\d+"
#F(([0-68-9]\d*)|(7\d{1}$))|P([0-13-46-9]|56)

# if name_to_be_replaced=="@", replace it with what is found in Q_group
name_to_be_replaced="@"


#------------------  {writed_field : DB_field}
writed_field_to_db_field={"PhysMin":"Y_Axis_Min",
                          "PhysMax":"Y_Axis_Max",}

def getSQL(component, table_name, field, name, conn, each_name, each_field,hasInserted):
    
    if(mode=="UPDATE" or (mode=="INSERT" and hasInserted==True)):
        
        sql = "update `" + conn["database"] + "`.`" + table_name + "` set "
        sql += field[each_field] + "='" + component[each_name][each_field] + "'"
        sql += " where Name='" + component[each_name][name] + "' limit 1"
        return sql
    
    elif(mode=="INSERT"):      
        sql = "insert `" + conn["database"] + "`.`" + table_name + "` set `name`='"+component[each_name][name]+"',`"+field[each_field]+"`='"+component[each_name][each_field]+"'"
        
        print(sql)
        return sql

# write into DB with component
def writeIntoDB(component,table_name,field,name=component_name):
    # Read port number from config.ini
        path = os.path.dirname(__file__)
        path=os.path.join(path, config_file_name)
        config = configparser.ConfigParser()
        config.read(path)
        conn={}
        conn["user"]= config.get("Database", "user")
        conn["password"] = config.get("Database", "password")
        conn["host"] = config.get("Database", "host")
        conn["database"] = config.get("Database", "database")
        #config.port = config.get("Database", "port")    
        print(conn)
    # connect to Mysql DB
        db = connector.connect(**conn)
        cursor = db.cursor()
        
    # execute the sql statement
        suc=0
        fail=0
        name_list=list(component.keys())
        for each_name in name_list:
            hasInserted=False    # only affects on INSERT mode
            for each_field in field:
                sql = getSQL(component, table_name, field, name, conn, each_name, each_field,hasInserted)
                if(mode=="INSERT" and hasInserted==False):
                    hasInserted=True
                print(sql)
                try:
                    cursor.execute(sql)
                    
                    suc+=1
                    print("query successfully!!")
                except Exception as e:
                    pass
                    fail+=1
                    print("query fail:",sql)
                    print(str(e))

        print("suc=",suc,"\nfail=",fail)
        db.commit()
        cursor.close()
        db.close()
            

# eliminate the end number if the number of this component is only one 
def delEndNumIfSingle(component,name,pattern):
    component_name_list=list(component.keys())
    for each_name in component_name_list:
        if(re.search(pattern, component[each_name][name])):
            print("find:",component[each_name][name])
            target=component[each_name][name][:-1]
            target+="2"
            print("search for:",target)
            for each_similar_name in component_name_list:
                print("via:",component[each_similar_name][name])
                if( component[each_similar_name][name]==target):
                    return component
            
            # cannot find the second one
            component[each_name][name]=target[:-1]
    return component  
            
            

# get component's name from Q_group (also return the group num)
def getNameFromGroup(name,component):
    component_name_list=list(component.keys())
    result_name="null"
    group="null"
    
    for each_name in component_name_list:
        property_list=list(component[each_name])
        user_name=component[each_name][component_name]
        for each_property in property_list:
            value=component[each_name][each_property]
            if (value==name):
                result_name=user_name+"."+each_property.lower()
                group=each_name
                print("[",each_name,"]\n",result_name)
                break
    
    print(name,result_name,group)
    return result_name,group

def setComponetNameWithPattern(mfc_component,Q_group,user_name,pattern):
    mfc_name_list=list(mfc_component.keys())
    
    for each_name in mfc_name_list:
        if(mfc_component[each_name][user_name]=="@"):
            name,group=getNameFromGroup(each_name,Q_group)
            mfc_component[each_name][user_name]=name
            mfc_component[each_name]["Group"]=group
            
            '''if(each_proverty.attrib["NAME"]==component_name and each_proverty.text=="@"):
                print("[",each_proverty,"]\nName=",each_proverty.text)'''
        
    

def printComponent(mfc_component):
    name_list=list(mfc_component.keys())
    for each_name in name_list:
    #OrderedDict(sorted(mfc_component[each_component]))
        print("[",each_name,"]\n",mfc_component[each_name],"\n\n")
    print("len= ",len(mfc_component))

def getDictElementAsPattern(pattern,dict):
    component=collections.OrderedDict()
    name_list=[]
    for each_component in dict:
        dict_name=each_component.attrib["NAME"]
        if(re.search(pattern, dict_name)):
            component.__setitem__(dict_name,collections.OrderedDict())
            
        else:
            continue
            
        for each_property in each_component:
            
            if((each_property.text!=None and each_property.text!='0')or each_property.attrib["NAME"]=="PhysMin"):
                name=each_property.attrib["NAME"]
                text=each_property.text
                #print("["+name+"]")
                #print(text)
                
                component[dict_name].__setitem__(name,text)
                if(name==component_name):
                    name_list.append(dict_name)
                        
                    #move "userName to the top of the dict"
                    component[dict_name].move_to_end(name, False)


    return component


def outputWithCSV(component):
    f = open("output.csv","w+",newline='')
    device_list=component.keys()
    
    #get attr_list
    for each_device in device_list:
        print(component[each_device])
        attr_list=component[each_device].keys()
        break
    
    row=["Id"]
    #write the columns' name
    for each_attr in attr_list:
        print(each_attr)
        row.append(each_attr)
    print(row)
    w=csv.writer(f)
    w.writerow(row)
    
    #write data
    
    for each_device in device_list:
        row=[]
        row.append(each_device)
        for each_attr in component[each_device]:
            value=component[each_device][each_attr]
            row.append(value)
        w.writerow(row)
            #row.append(e)
            

tree = etree.parse('mfc.xml')
root = tree.getroot()


'''
count=0
# get the device name under the root
for each_component in root:
    if(each_component.attrib["NAME"]):
        print(each_component.attrib["NAME"])
        count+=1
print(count,"\n\n\n")
count=0

name_list=[]'''

mfc_component=collections.OrderedDict()

# It first processes the components for FXX and PXX group,while QXX group will be processed later 


mfc_component=getDictElementAsPattern(device_pattern,root) 
 
printComponent(mfc_component)



# Q group

Q_group=collections.OrderedDict()

Q_group=getDictElementAsPattern(Q_group_pattern, root)

printComponent(Q_group)


##setComponetNameWithPattern(mfc_component,Q_group,component_name, name_to_be_replaced)



##mfc_component=delEndNumIfSingle(mfc_component,component_name,"push|inject")
printComponent(mfc_component)

if(CSV_Output==True):
    outputWithCSV(mfc_component)

if(Database_write_back==True):
    writeIntoDB(mfc_component,"mfc_config",writed_field_to_db_field)

