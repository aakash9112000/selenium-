import unittest
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# #  here is below code for the company build and due to error i am opening it directly 

Username = "aakashyadav112000@gmail.com"
Password = "rainbow@123"

First_name  = "anjali"
Last_name  = "Yadav"
About =" Employe"
Design  = "Senior Developer"
City ="jaipur"
Address = " malviya nagar "
Company ="innovation with us"
C_city ="chomu"
C_address ="vaishali"
C_about ="C.T.O"
C_site = "https://testing.timestint.com"
C_code =302012
Phone =9116582228
Email = "8302765048adarshyadav@gmail.com"
Mob =9090876545

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

driver.maximize_window()

driver.find_element_by_class_name("mat-raised-button").click()
print("working")
time.sleep(3) 


driver.find_element_by_xpath('//*[@id="mat-expansion-panel-header-1"]/span[1]/mat-panel-title').click()
driver.find_element_by_xpath('//*[@id="cdk-accordion-child-1"]/div/a[1]/div').click()

time.sleep(2)
urls ="https://dashtest.timestint.com/company/add"
# driver = webdriver.Chrome("/home/aakash/Downloads/chromedriver")
driver.get(urls)





company = driver.find_element_by_id("mat-input-0")
company.click()
company.send_keys(Company)


industry = driver.find_element_by_id("mat-select-value-3")
industry.click()

it = driver.find_element_by_id('mat-select-2-panel')
it.click()



mob = driver.find_element_by_id("mat-input-2")
mob.click()
mob.send_keys(Mob)

c_site = driver.find_element_by_id("mat-input-3") 
c_site.click()
c_site.send_keys(C_site)


coun = driver.find_element_by_id("mat-select-4")
coun.click()

Coun = driver.find_element_by_id('mat-select-4-panel')
Coun.click()




state = driver.find_element_by_id("mat-select-value-7")
state.click()

State = driver.find_element_by_id("mat-select-6-panel")
State.click()


c_city = driver.find_element_by_id("mat-input-4")
c_city.click()
c_city.send_keys(C_city)

c_address = driver.find_element_by_id("mat-input-6")
c_address.click()
c_address.send_keys(C_address)



c_about = driver.find_element_by_id("mat-input-7")
c_about.click()
c_about.send_keys(C_about)


c_code = driver.find_element_by_id("mat-input-5") 
c_code.click()
c_code.send_keys(C_code)




time= driver.find_element_by_id("mat-select-value-9")
time.click()

c_time = driver.find_element_by_id("mat-select-8-panel")
c_time.click()


driver.find_element_by_xpath('/html/body/app-root/app-core/mat-sidenav-container/mat-sidenav-content/app-company-form/div/mat-card/mat-card-content/form/button[1]').click()


