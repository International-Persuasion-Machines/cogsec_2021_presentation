import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
name = sys.argv[1]
email = sys.argv[2]
password = sys.argv[3]

options = webdriver.ChromeOptions() 
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)
driver.get("http://demo-rails-app-testing.ipm-corporation.com/signup?disallow_selenium=true")
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


