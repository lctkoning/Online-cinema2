import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)  # Optional argument, if not specified will search path.

start_url = 'http://localhost:8080/cinema/movies/page/1'
driver.get(start_url)

def login_test():
    driver.find_element_by_id('username').send_keys('admin')
    driver.find_element_by_id('password').send_keys('admin')
    driver.find_element_by_name('submit').click()
    print ("Login works!")
    
login_test()

def movielisttest():
    movielist = driver.find_elements_by_class_name('title')

    if len(movielist) == 5:
        print('Number of movies are correct')

movielisttest()


driver.quit()