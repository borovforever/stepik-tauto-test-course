import time

import os

from selenium import webdriver


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt') 
link = "http://suninjuly.github.io/file_input.html"
driver = webdriver.Chrome("chromedriver.exe")
driver.get(link)
driver.find_element_by_xpath("//input[@name='firstname']").send_keys('Jake')
driver.find_element_by_xpath("//input[@name='lastname']").send_keys('Stark')
driver.find_element_by_xpath("//input[@name='email']").send_keys('test@sdsd.dd')
driver.find_element_by_xpath("//input[@type='file']").send_keys(file_path)
driver.find_element_by_xpath("//button[@type='submit']").click()

time.sleep(10)

   
