import unittest
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

Username = "aakashyadav112000@gmail.com"
Password = "rainbow@123"
has_failures = []

class MyGoogleTest(unittest.TestCase):
    # if  result.wasSuccessful():
    def tearDown(self):
        print("failedddd")

    def test_login(self):
        url ="https://dashtest.timestint.com/login"
        driver = webdriver.Chrome("/home/aakash/Downloads/chromedriver")
        driver.get(url)    
        # print("*** test failed")
        # time.sleep(4)
        username = driver.find_element_by_id("mat-input-01")
        password = driver.find_element_by_id("mat-input-11")
        # time.sleep(6)
        username.send_keys(Username)
        password.send_keys(Password)

        driver.find_element_by_class_name("mat-raised-button").click()

        print("working")
        time.sleep(6)
    
    # if  result.wasSuccessful():
    #         print("*** test failed")
        
if __name__ == '__main__':
    # var2="successful completed"
    # print(var2)
    unittest.main()

print("complete")