print("hello")

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


Username = "aakashyadav112000@gmail.com"
Password = "rainbow@123"

firstname = "suraj"
lastname = "yadav"
email ="suraj@gmail.com"
Phone =9911223344
Country = +91
Password ="rainbow@123"
C_Password ="rainbow@123"


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


print("signup")




urls ="https://dashtest.timestint.com/signup"

driver = webdriver.Chrome("/home/aakash/Downloads/chromedriver")
driver.get(urls)


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


fname.send_keys(firstname)
lname.send_keys(lastname)
Email.send_keys(email)
phone.send_keys(Phone)
# country.selectByVisibleText("INDIA")
password.send_keys(Password)
c_password.send_keys(C_Password)


driver.find_element_by_class_name("mat-raised-button").click()
print("working")