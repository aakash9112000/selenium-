# lst = [1,2,3,4,'Python']

# https://dashtest.timestint.com/profile
import unittest
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


Username = "aakashyadav112000@gmail.com"
Password = "rainbow@123"

First_name  = "anjali"
Last_name  = "Yadav"
About =" Employe"
Design  = "Senior Developer"
City ="jaipur"
Address = " malviya nagar "

Phone = 9898989898
Email = "8302765048adarshyadav@gmail.com"

url ="https://dashtest.timestint.com/login"
driver = webdriver.Chrome("/home/aakash/Downloads/chromedriver")
driver.get(url)
username = driver.find_element_by_id("mat-input-0")
print(username)
username.clear()
password = driver.find_element_by_id("mat-input-1")
# time.sleep(6)
username.send_keys(Username)
password.send_keys(Password)

driver.find_element_by_class_name("mat-raised-button").click()

print("working")
time.sleep(7) 
driver.find_element_by_class_name("mat-button").click() 
driver.find_element_by_xpath('//button[text()="Profile"]').click()
print('click')
time.sleep(7) 
driver.find_element_by_id("mat-tab-label-0-1").click() 

first_name = driver.find_element_by_id('mat-input-2')
first_name.clear()
print("kkkkkkkkkkkkkk",first_name)
first_name.send_keys(First_name)

last_name = driver.find_element_by_id('mat-input-3')
last_name.clear()
print("kkkkkkkkkkkkkk",last_name)
last_name.send_keys(Last_name)



# email

# email = driver.find_element_by_id('mat-input-4')
# email.click()
# email.clear()
# print("start of email")
# print("kkkkkkkkkkkkkk",email)
# email.send_keys(Email)
# print("last of email")



phone = driver.find_element_by_id('mat-input-5')
phone.clear()
print("kkkkkkkkkkkkkk",phone)
phone.send_keys(Phone)


design = driver.find_element_by_id('mat-input-6')
design.clear()
print("kkkkkkkkkkkkkk",design)
design.send_keys(Design)

about = driver.find_element_by_id('mat-input-8')
about.clear()
print("kkkkkkkkkkkkkk",about)
about.send_keys(About)


country = driver.find_element_by_id("mat-select-value-5")
country.click()
# country.click()

cl =driver.find_element_by_id("mat-select-4-panel")
cl.click()
# mat-option-3  mat-select-value-21

state = driver.find_element_by_id("mat-select-value-7")
state.click()
# country.click()

st =driver.find_element_by_id("mat-option-3") 
st.click() 

city = driver.find_element_by_id('mat-input-9')
city.clear()
print("kkkkkkkkkkkkkk",city)
city.send_keys(City)

address = driver.find_element_by_id('mat-input-11')
address.clear()
print("kkkkkkkkkkkkkk",address)
address.send_keys(Address)

# mat-focus-indicator buttonSubmit mat-raised-button mat-button-base

# driver.find_element_by_class_name("mat-focus-indicator").click() 

# driver.find_element_by_class_name("mat-focus-indicator").click() 
driver.find_element_by_xpath('//*[@id="mat-tab-content-0-1"]/div/form/div[2]/button').click()

time.sleep(45)
driver.find_element_by_id('mat-input-4').clear()


first_name = driver.find_element_by_id('mat-input-2').clear()
first_name.send_keys("anjali")
time.sleep(45)



# '//*[@id="mat-tab-content-0-1"]/div/form/div[2]/button'
# '//*[@id="mat-expansion-panel-header-1"]/span[1]/mat-panel-title'