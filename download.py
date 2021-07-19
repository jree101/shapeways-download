#!/usr/bin/env python
import os
from selenium import webdriver


CREATIONS_LIST = 'https://www.shapeways.com/designer/mz4250/creations'

driver = webdriver.Chrome('./chromedriver')#uses google chrome
wait = ui.WebDriverWait(driver, 60) # timeout after 60 seconds, useful for antibot measures
    

def site_login():
    driver.get ('https://www.shapeways.com/login')#websites login
    driver.find_element_by_id('login_username').send_keys('username')#replace 'username' with username
    driver.find_element_by_id ('login_password').send_keys('password')#replace 'password' with password
    submit = driver.find_element_by_id("sign_in_button")#find sign in button
    submit.click()#click on submit button
    results = wait.until(lambda driver: driver.find_elements_by_class_name('site-main'))#wait for site to login and load
    

def get_first():
    driver.get('https://www.shapeways.com/designer/mz4250/creations')#site to start downloading from
    elements = driver.find_elements_by_css_selector('a.product-url')#finds products on page
    links = [el.get_attribute('href') for el in elements]# gets links and adds them to a list/array. Currently causes duplicates of all links.
#    for url in links[1:]:#
#        driver.execute_script('window.open("{}", "_blank");'.format(url))#should open all links in list
#        element2 = driver.find_element_by_css_selector('a.btn')#finds download link
#        element2.click()should click on download link
    print(links)
    # needs to go to next page and repeat process.
    
    
site_login()

get_first()

driver.quit()
