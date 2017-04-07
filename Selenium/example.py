from selenium import webdriver
import time

chrome_path = "chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
web = webdriver.Chrome(chrome_path)

web.get('http://www.cwb.gov.tw/V7/')
web.set_window_position(0,0) #瀏覽器位置
web.set_window_size(700,700) #瀏覽器大小
time.sleep(5)

web.find_element_by_link_text('天氣預報').click() #點擊頁面上"天氣預報"的連結
time.sleep(5)

web.close()