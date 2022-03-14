print("hello")
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


Username = "aakashyadav112000@gmail.com"
Password = "rainbow@123"


url ="https://dashtest.timestint.com/login"

driver = webdriver.Chrome("/home/aakash/Downloads/chromedriver")
driver.get(url)


# time.sleep(4)
username = driver.find_element_by_id("mat-input-0")
password = driver.find_element_by_id("mat-input-1")
# time.sleep(6)
username.send_keys(Username)
password.send_keys(Password)

driver.find_element_by_class_name("mat-raised-button").click()

print("working")
time.sleep(7) 
driver.find_element_by_class_name("mat-button").click() 
driver.find_element_by_xpath('//button[text()="Logout"]').click()
print('click')
 
time.sleep(2) 
# Kill the browser 
driver.quit() 

print("working")