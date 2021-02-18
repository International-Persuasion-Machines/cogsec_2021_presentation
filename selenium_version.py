import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
name = sys.argv[1]
email = sys.argv[2]
password = sys.argv[3]

driver = webdriver.Firefox()
driver.get("http://demo-rails-app-testing.ipm-corporation.com/signup")
element = driver.find_element_by_id("user_name")
element.send_keys(name)
element = driver.find_element_by_id("user_email")
element.send_keys(email)
element = driver.find_element_by_id("user_password")
element.send_keys(password)
element = driver.find_element_by_id("user_password_confirmation")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()


