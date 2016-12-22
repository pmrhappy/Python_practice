import sys
print "Python : ",sys.version

package_list=["numpy","scipy","pandas","sklearn"]

modules = map(__import__, package_list)
for each_package in package_list:
    print each_package," : ",modules[0].__version__

