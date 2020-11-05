import document as document

from selenium import  webdriver

import math

def calc(x):
    """Math formula"""
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome('chromedriver.exe')
link = "http://suninjuly.github.io/execute_script.html"
driver.get(link)

field_x = driver.find_element_by_id('input_value')
x = field_x.text
y = calc(x)
fill = driver.find_element_by_xpath("//input[@id='answer']").send_keys(y)
robot = driver.find_element_by_xpath("//input[@id='robotCheckbox']").click()
driver.execute_script("return arguments[0].scrollIntoView(true);", robot)
button = document.getElementsByTagName("robotsRule")[0];
return button.scrollIntoView(true)


