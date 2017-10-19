#!/usr/bin/env python
import os
from selenium import webdriver

LOGIN_URL = 'https://www.shapeways.com/login'
LOGIN_USER = os.environ['LOGIN_USER']
LOGIN_PASS = os.environ['LOGIN_PASS']

CREATIONS_LIST = 'https://www.shapeways.com/designer/mz4250/creations'

driver = webdriver.Chrome()


def login():
    driver.get(LOGIN_URL)

    username = driver.find_element_by_id("login_username")
    password = driver.find_element_by_id("login_password")
    submit = driver.find_element_by_id("sign_in_button")

    username.send_keys(LOGIN_USER)
    password.send_keys(LOGIN_PASS)
    submit.click()


def get_first():
    driver.get(CREATIONS_LIST)

    elements = driver.find_elements_by_css_selector('a.product-url')
    links = [el.get_attribute('href') for el in elements]
    print(links)


login()
get_first()

driver.quit()
