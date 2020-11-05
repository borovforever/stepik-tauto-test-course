import time
import math

import unittest

import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec


# answer = math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():

    # options.add_argument("--headless")
    print("\nstart browser for test..")
    options = Options()
    browser = webdriver.Firefox(executable_path="geckodriver.exe")
    browser.implicitly_wait(10)
    browser.set_page_load_timeout(10)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()

def calc(x):
    """Math formula"""
    return str(math.log(int(time.time() + 1.3)))

@pytest.mark.parametrize('links',
                             ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                              "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                              "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                              "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, links):
    browser.get(links)
    browser.implicitly_wait(10)
    WebDriverWait(browser, 20).until(ec.element_to_be_clickable((By.XPATH, "//div//textarea"))).send_keys(
        str(math.log(int(time.time() + 1.3))))
    WebDriverWait(browser, 20).until(
        ec.element_to_be_clickable((By.XPATH, "//div//button[@class='submit-submission']"))).click()
    success_test = WebDriverWait(browser, 20).until(
        ec.visibility_of_element_located((By.XPATH, "//pre[@class='smart-hints__hint']"))).text
    if success_test:
        print(success_test)
        assert True
    else:
        print(success_test)
        assert False, \
            f"Test {success_test} failed."
