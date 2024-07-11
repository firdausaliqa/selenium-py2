from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#select browser and open base url
browser = webdriver.Chrome()
browser.get('https://saucedemo.com/')

#find element by (NAME,XPATH, ID)
browser.find_element(By.NAME, '').send_keys()