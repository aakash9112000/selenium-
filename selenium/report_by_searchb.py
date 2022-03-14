import unittest
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
url ="https://www.google.co.in/"
has_failures = []


First_name  = "anjali"
Last_name  = "Yadav"
About =" Employe"
Design  = "Senior Developer"
City ="jaipur"
Address = " malviya nagar "

Phone =9116582228
Email = "8302765048adarshyadav@gmail.com"

class MyGoogleTest(unittest.TestCase):

    def test_login(self):
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
        # time.sleep(7) 
        # driver.find_element_by_class_name("mat-button").click() 
        # driver.find_element_by_xpath('//button[text()="Logout"]').click()
        # print('click')
        
        time.sleep(2) 
        # Kill the browser 
        driver.quit()

    def test_logout(self):
        url ="https://dashtest.timestint.com/login"

        driver = webdriver.Chrome("/home/aakash/Downloads/chromedriver")
        driver.get(url)


        time.sleep(4)
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

    def test_profile_update(self):


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











    def test_signup(self):
        url ="https://dashtest.timestint.com/signup"
        driver = webdriver.Chrome("/home/aakash/Downloads/chromedriver")
        driver.get(url)    
        # print("*** test failed")
        # time.sleep(4)
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
        time.sleep(6)

        
if __name__ == '__main__':
    # var2="successful completed"
    # print(var2)
    unittest.main()

print("complete")