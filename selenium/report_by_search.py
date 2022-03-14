
import unittest
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

firstname = "suraj"
lastname = "yadav"
email ="suraj@gmail.com"
Phone =9911223344
Country = +91
Password ="rainbow@123"
C_Password ="rainbow@123"
url ="https://www.google.co.in/"
has_failures = []

class MyGoogleTest(unittest.TestCase):
    # if  result.wasSuccessful():
    def tearDown(self):
        print("failedddd")

    def test_login(self):
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






















__author__ = 'rahul'
 
import unittest
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class MyGoogleTest(unittest.TestCase):
    driver = webdriver.Chrome("/home/aakash/Downloads/chromedriver")
    driver.implicitly_wait(0.5)
    driver.get("https://dashtest.timestint.com/signup")
    # driver.get("https://www.google.com/")
    # m = driver.find_element_by_name("q")
    # #enter search text
    # m.send_keys("sachin Tendulkar")
    # time.sleep(0.2)
    # m.send_keys(Keys.ENTER) 
    
    
def tearDown(self):
        # Close the browser.
    self.driver.close()
        
        
if __name__ == '__main__':
    unittest.main()

print("complete")




 

# # class MyWikiTestCase(unittest.TestCase):
 
# #     def setUp(self):
# #         self.driver = webdriver.google()
# #     def test_Wiki(self):
# #         driver = self.driver
# #         driver.maximize_window()
        


# driver.find_element_by_class_name('gLFyf').clear()
# m =driver.find_element_by_class_name('gLFyf').send_keys('Sachin Tendulkar')
# time.sleep(0.2)
# #perform Google search with Keys.ENTER
# m.send_keys(Keys.ENTER)




# # driver.find_element_by_class_name('gLFyf').click()   
# # driver.find_element_by_class_name('gLFyf gsfi').click()
# driver.find_element_by_css_selector("gLFyf").click()
# print("working")

# print("working")
 
 
# # def tearDown(self):
# #     self.driver.quit()
 
 
# # if __name__ == '__main__':
# #     unittest.main()











# # __author__ = 'rahul'
 
# # import unittest
# # from selenium import webdriver
 
 
# # class MyGoogleTest(unittest.TestCase):
# #     def setUp(self):
# #         self.driver = webdriver.google()
 
# #     def test_GoogleTest(self):
# #         driver = self.driver
# #         driver.maximize_window()
# #         driver.get('https://www.youtube.com/')
 
# #         driver.find_element_by_id('masthead-search-term').clear()
# #         driver.find_element_by_id('masthead-search-term').send_keys('Metallica')
# #         driver.find_element_by_id('search-btn').click()
 
 
 
# # if __name__ == '__main__':
# #     unittest.main()








# url ="https://www.google.co.in/"

# driver = webdriver.Chrome("/home/aakash/Downloads/chromedriver")
# driver.get(url)