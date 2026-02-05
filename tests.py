import time

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pages
import data

class Test_The_Super_Shopping_Pro ():
    driver = webdriver.Chrome()
    driver.get(data.URL)
    def test_login(self):
        test_email = data.Email
        test_pass = data.Password
        pages.login.login_page(self).click()
        pages.login.emailBox(self,test_email)
        pages.login.passwordBox(self,test_pass)
        time.sleep(5)
        pages.login.signin_button(self).click()


