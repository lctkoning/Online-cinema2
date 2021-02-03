import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pytest
import sys



def test_lambdatest_todo_app():
    chrome_options = Options()

    chrome_options.add_argument("--headless")

    chrome_options.binary_location = "/opt/google/chrome/chrome"  # chrome binary location specified here

    chrome_options.add_argument("--no-sandbox")  # bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)  # Optional argument, if not specified will search path.

    start_url = 'http://localhost:8080/cinema/movies/page/1'
    driver.get(start_url)
    driver.find_element_by_id('username').send_keys('admin')
    driver.find_element_by_id('password').send_keys('admin')
    driver.find_element_by_name('submit').click()
    print ("Login works!")
    driver.find_elements_by_class_name('title')
    sleep(2)
    driver.close()