import selenium
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import data

class login:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(data.URL)
    def emailBox(self, setUser):
        element = self.driver.find_element(By.ID, "customer_email")
        element.send_keys(setUser)
        return element
    def passwordBox(self, setPass):
        element = self.driver.find_element(By.ID, "customer_password")
        element.send_keys(setPass)
        return element
    def login_page(self):
        return self.driver.find_element(By.XPATH, '//*[@id="customer_login_link"]')
    def signin_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#customer_login > div.action_bottom > input')
class signin:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(data.URL)
    def signup_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#customer_register_link')
    def nameBox(self, setName):
        element = self.driver.find_element(By.CSS_SELECTOR, '#first_name')
        element.send_keys(setName)
        return element