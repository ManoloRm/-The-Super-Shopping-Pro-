import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pages
import data

class Test_The_Super_Shopping_Pro ():
    driver=webdriver.Chrome()
    driver.get(data.URL)

    def login(self):
        pages.login.login_page().click()
        pages.login.emailBox().send_keys("<EMAIL>")
        pages.login.passwordBox().send_keys("<PASSWORD>")
        assert pages.login.emailBox().get_attribute("value") == "<EMAIL>"
