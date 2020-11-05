from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    """Math formula"""
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome('chromedriver.exe')
browser.implicitly_wait(12)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
browser.find_element_by_id("book").click()
x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)
answer = browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)
submit_btn = browser.find_element_by_xpath("//button[@type='submit']").click()

time.sleep(10)


