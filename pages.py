import selenium
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import data

class login:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(data.URL)
    def emailBox(self):
        return self.driver.find_element(By.ID, "customer_email")
    def passwordBox(self):
        return self.driver.find_element(By.ID, "customer_password")