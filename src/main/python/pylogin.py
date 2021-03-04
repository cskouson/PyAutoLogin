from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from getpass import getpass
import json

#get list of credentials from local json file
file = open('creds.json')
creds = json.load(file)

#temp creds
username = creds["netflix"]["username"]
password = creds["netflix"]["password"]


#driver setup
driver = webdriver.Firefox()
#delay until full page load
#wait = WebDriverWait(driver, 10)

#send get request
driver.get("https://www.netflix.com/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse")
#wait.until(presence_of_element_located(By.id("id_userLoginId")))

#fill netflix fields and submit
driver.find_element_by_id('id_userLoginId').send_keys(username)
driver.find_element_by_id('id_password').send_keys(password)
driver.find_element_by_class_name('btn-submit').submit()

