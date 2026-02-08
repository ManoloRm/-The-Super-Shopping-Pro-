import selenium
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import data

class login:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(data.URL)
    def emailBox(self, setUser):
        return self.driver.find_element(By.ID, "customer_email").send_keys(setUser)
    def passwordBox(self, setPass):
        return self.driver.find_element(By.ID, "customer_password").send_keys(setPass)
    def login_page(self):
        return self.driver.find_element(By.XPATH, '//*[@id="customer_login_link"]')
    def signin_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#customer_login > div.action_bottom > input')
    def captcha_select(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#account > div:nth-child(12)')