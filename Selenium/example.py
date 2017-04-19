from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import re
import configparser
import base64
import datetime
import traceback
from fuzzywuzzy import fuzz

def get_setting_params(setting_file_path):
    config_parser = configparser.RawConfigParser()
    config_parser.optionxform = lambda option: option
    config_parser.read("setting.ini")
    return config_parser._sections['basic']['f1'], config_parser._sections['basic']['f2'], config_parser._sections['basic']['f3']

def strip_string_list(token, str_list):
    for s in range(len(str_list)):
        str_list[s] = str_list[s].split(token)[0]
    return str_list

def get_new_books_set_diff(result, last_result):
    last_result = strip_string_list(" /", last_result)
    result = strip_string_list(" /", result)
    new_books = list(set(result) - set(last_result))
    return new_books

def get_new_books_fuzzy(result, last_result):
    new_books = []
    for each_new_book in result:
        for b in range(len(last_result)):
            if fuzz.ratio(each_new_book, last_result[b]) >= 90:
                break
            elif b == len(last_result)-1:
                #print(each_new_book, "\n", last_result[b])
                #print("fuzz: ", fuzz.ratio(each_new_book, last_result[b]), "\n")
                new_books.append(each_new_book)
    return new_books
        
    
if __name__ == '__main__':
    while True:
        try:
            f1, f2, f3 = get_setting_params("setting.ini")
            chrome_path = "chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
            
            chrome_options = Options()
            chrome_options.add_argument("--window-position=-1900,200")
            chrome_options.add_argument("--window-size=500,500")
            
            web = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
            #web.set_window_position(-1900,200) #瀏覽器位置
            #web.set_window_size(500,500) #瀏覽器大小
            web.get(base64.b64decode(f3.encode('ascii')).decode('ascii'))

            
            web.find_element_by_name("USER").send_keys(base64.b64decode(f1.encode('ascii')).decode('ascii'))
            web.find_element_by_name("PASSWORD").send_keys(base64.b64decode(base64.b64decode(f2.encode('ascii'))).decode('ascii'))
            web.find_element_by_name("Submit").click()
            web.find_element_by_xpath("/html/body/table[4]/tbody/tr/td/table/tbody/tr/td[6]/a").click()

            #web.find_element_by_id("first6").find_element_by_id("more").click()
            #print(web.window_handles)
            #web.switch_to_window(web.window_handles[1])
            #time.sleep(2)
            #elements = web.find_elements_by_css_selector("*")
            
            web.find_element_by_xpath('/html/body/table[7]/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/select/option[2]').click()
            # type_selector = web.find_elements_by_name('MATERIAL')[0]
            # for option in type_selector.find_elements_by_tag_name('option'):
                # if option.text == "BOOK":
                    # option.click()
                    # break
            
            web.find_elements_by_name('cmd_click')[0].click()
            result = []
            next_index_xpath = '/html/body/div[2]/a'
            while True:
                for i in range(2, 22):
                    try:
                        element = web.find_elements_by_xpath('/html/body/table[8]/tbody/tr[' + str(i) + ']/td[3]/a')[0]
                        #print("element.text: ", element.text.encode())
                        result.append((element.text + '\n'))
                    except Exception as err:
                        if type(err) is IndexError:
                            break
                        else:
                            print(traceback.format_exc())
                try:
                    web.find_elements_by_xpath(next_index_xpath)[0].click()
                    next_index_xpath = '/html/body/div[2]/a[2]'
                except Exception as err:
                    if type(err) is IndexError:
                        break
                    else:
                        print(traceback.format_exc())
            #pattern = re.compile(r"^(gvList_)[a-z0-9]*(_lbnCname)$")

            # result = []
            # for element in elements:
                #print("id= ", element.get_attribute("id"))
                # if pattern.match(element.get_attribute("id")):
                    #print(element.text)
                    # result.append(element.text)
            # print("=========================\n\n")
            
            with open("book_list.txt", "a+", encoding='utf8') as result_file:
                result_file.seek(0)
                last_result = result_file.read().splitlines()
                
            with open("book_list.txt", "w", encoding='utf8') as result_file:
                for each_book_name in result:
                    result_file.write(each_book_name)
            print("books have been saved!!")        
            #new_books = get_new_books_set_diff(result, last_result)
            new_books = get_new_books_fuzzy(result, last_result)
            
            if len(new_books) > 0:
                new_books_list_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "new_" + str(datetime.datetime.now().time()).replace(':', '_') + ".txt")
                with open(new_books_list_file_path, "w", encoding='utf8') as new_file:
                    if len(last_result) > 0: 
                        print(">>>New books :")
                        for each_new_book in new_books:
                            #print(each_new_book)
                            new_file.write(each_new_book)
                os.system("start notepad " + new_books_list_file_path)
            else:
                print("No new books!!>_<")
            
            web.close()
            web.quit()
            time.sleep(600)
            
        except Exception as e:
            print(traceback.format_exc())
            print("error occurs!! retrying...")
            time.sleep(5)
        
        
        
        
        