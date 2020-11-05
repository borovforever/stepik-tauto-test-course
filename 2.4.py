import time

import os

from selenium import webdriver

import math

try:

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt') 
    link = "http://suninjuly.github.io/wait1.html"

    driver = webdriver.Chrome("chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get(link)
    driver.find_element_by_xpath("//button[@id='verify']").click()

    message = driver.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    time.sleep(5)
    driver.quit()