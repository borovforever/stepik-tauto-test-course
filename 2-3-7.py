import time

import os

from selenium import webdriver

import math

def calc(x):
    """Math formula"""
    return str(math.log(abs(12*math.sin(int(x)))))


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt') 
link = "http://suninjuly.github.io/alert_accept.html"
driver = webdriver.Chrome("chromedriver.exe")
driver.get(link)
driver.find_element_by_xpath("//button").click()
confirm = driver.switch_to.alert
confirm.accept()
x_element = driver.find_element_by_xpath("//span[@id='input_value']")
x = x_element.text
y = calc(x)
answer = driver.find_element_by_xpath("//input[@id='answer']").send_keys(y)
submit_btn = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(10)
