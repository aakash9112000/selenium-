print("hello")
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
import time
from selenium.webdriver.chrome.service import Service

firstname = "suraj"
lastname = "yadav"
email ="suraj@gmail.com"
Phone =9911223344
Country = +91
Password ="rainbow@123"
C_Password ="rainbow@123"
url ="https://dashtest.timestint.com/signup"

driver = webdriver.Chrome("/home/aakash/Downloads/chromedriver")
driver.get(url)


time.sleep(4)





fname= driver.find_element_by_id("mat-input-0")
lname= driver.find_element_by_id("mat-input-1")
phone= driver.find_element_by_id("mat-input-3")
Email= driver.find_element_by_id("mat-input-2")

password= driver.find_element_by_id("mat-input-4")
c_password= driver.find_element_by_id("mat-input-5")
time.sleep(1) 
# c_password= driver.find_element_by_class_name("mat-option-text").click()

country = driver.find_element_by_id("mat-select-0")
country.click()
driver.find_element_by_class_name("mat-option-text").click()
# mat-option-3

fname.send_keys(firstname)
lname.send_keys(lastname)
Email.send_keys(email)
phone.send_keys(Phone)
# country.selectByVisibleText("INDIA")
password.send_keys(Password)
c_password.send_keys(C_Password)


driver.find_element_by_class_name("mat-raised-button").click()
print("working")