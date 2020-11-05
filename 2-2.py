from selenium import webdriver

import time

import math


def calc(x):
    """Math formula"""
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    driver = webdriver.Chrome('C:/stepik automations course/chromedriver.exe')
    driver.get(link)

    x_element = driver.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    answer = driver.find_element_by_xpath("//input[@id='answer']").send_keys(y)
    robot_checkbox = driver.find_element_by_xpath("//input[@id='robotCheckbox']").click()
    robots_rule = driver.find_element_by_xpath("//input[@id='robotsRule']").click()
    submit_btn = driver.find_element_by_xpath("//button[@type='submit']").click()