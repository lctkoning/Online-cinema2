import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pytest
import sys
from time import sleep


class Testcinema():
    @pytest.fixture()
    def setup(self):
        chrome_options = Options()

        chrome_options.add_argument("--headless")

        chrome_options.binary_location = "/opt/google/chrome/chrome"  # chrome binary location specified here

        chrome_options.add_argument("--no-sandbox")  # bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        chrome_options.add_argument("--disable-gpu")

        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)  # Optional argument, if not specified will search path.
        yield
        self.driver.close()
        #start_url = 'http://localhost:8080/cinema/movies/page/1'
        #driver.get(start_url)
        
    def test_login(self, setup):
        self.driver.get('http://localhost:8080/cinema/movies/page/1')
        self.driver.find_element_by_id('username').send_keys('admin')
        self.driver.find_element_by_id('password').send_keys('admin')
        self.driver.find_element_by_name('submit').click()
        assert self.driver.title=="Cinema"

    def test_movies(self, setup):
        self.driver.find_elements_by_class_name('title')
        assert self.driver.title=="Cinema"