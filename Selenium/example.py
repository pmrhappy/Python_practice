from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import re
import configparser
import base64
import datetime
import traceback

def get_setting_params(setting_file_path):
    config_parser = configparser.RawConfigParser()
    config_parser.optionxform = lambda option: option
    config_parser.read("setting.ini")
    return config_parser._sections['basic']['f1'], config_parser._sections['basic']['f2'], config_parser._sections['basic']['f3']

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


            web.find_element_by_id("first6").find_element_by_id("more").click()
            #print(web.window_handles)
            web.switch_to_window(web.window_handles[1])
            time.sleep(2)
            elements = web.find_elements_by_css_selector("*")
            pattern = re.compile(r"^(gvList_)[a-z0-9]*(_lbnCname)$")

            result = []
            for element in elements:
                #print("id= ", element.get_attribute("id"))
                if pattern.match(element.get_attribute("id")):
                    #print(element.text)
                    result.append(element.text)
            print("=========================\n\n")
            
            with open("book_list.txt", "a+") as result_file:
                result_file.seek(0)
                last_result = result_file.read().splitlines()
                result_file.truncate(0)
                for each_book_name in result:
                    result_file.write(each_book_name + "\n")
                    
            new_books = list(set(result) - set(last_result))
            if len(new_books) > 0:
                new_books_list_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "new_" + str(datetime.datetime.now().time()).replace(':', '_') + ".txt")
                with open(new_books_list_file_path, "w") as new_file:
                    if len(last_result) > 0: 
                        print(">>>New books :")
                        for each_new_book in new_books:
                            print(each_new_book)
                            new_file.write(each_new_book + "\n")
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
        
        
        
        
        