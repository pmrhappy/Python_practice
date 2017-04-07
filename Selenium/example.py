
from selenium import webdriver

import time
import re
import configparser

def get_setting_params(setting_file_path):
    config_parser = configparser.RawConfigParser()
    config_parser.optionxform = lambda option: option
    config_parser.read("setting.ini")
    return config_parser._sections['basic']['id'], config_parser._sections['basic']['pw'], config_parser._sections['basic']['url']

id, pw, url = get_setting_params("setting.ini")
chrome_path = "chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
web = webdriver.Chrome(chrome_path)

web.get(url)

web.set_window_position(0,0) #瀏覽器位置
web.set_window_size(1700,1700) #瀏覽器大小
web.find_element_by_name("USER").send_keys(id)
web.find_element_by_name("PASSWORD").send_keys(pw)
web.find_element_by_name("Submit").click()


web.find_element_by_id("first6").find_element_by_id("more").click()
#print(web.window_handles)
web.switch_to_window(web.window_handles[1])

elements = web.find_elements_by_css_selector("*")
pattern = re.compile(r"^(gvList_)[a-z0-9]*(_lbnCname)$")

result = []
for element in elements:
    #print("id= ", element.get_attribute("id"))
    if pattern.match(element.get_attribute("id")):
        print(element.text)
        result.append(element.text)
with open("book_list.txt", "w") as result_file:
    for each_book_name in result:
        result_file.write(each_book_name + "\n")
time.sleep(5)


#web.close()