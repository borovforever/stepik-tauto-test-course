
import time

from selenium import webdriver

import math

from selenium.webdriver.support.select import Select

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec



link = "https://cpstaging.snatch.cloud/"
driver = webdriver.Chrome("chromedriver.exe")
driver.get(link)
driver.find_element_by_xpath("//input[@name='email']").send_keys('ioleynik+autotest@zuzex.com')
driver.find_element_by_xpath("//input[@name='password']").send_keys('Monster12a')
driver.find_element_by_xpath("//span[@translate='auth.signIn']").click()
driver.find_element_by_xpath("//a[@data-test='route-bots']").click()
i = driver.find_elements_by_xpath(".//*[@data-test='bot-action-menu']")
i[0].click()
#driver.find_element_by_xpath("//*[@data-test='bot-action-delete']").click()


