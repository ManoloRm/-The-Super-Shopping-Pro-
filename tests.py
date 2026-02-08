import utils
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
        pages.login.emailBox(self, test_email)
        pages.login.passwordBox(self, test_pass)
        pages.login.signin_button(self).click()

        from utils import wait_for_element
        from selenium.webdriver.common.by import By
        captcha_locator = (By.ID, "ID_DEL_CAPTCHA")
        try:
            captcha_btn = wait_for_element(self.driver, captcha_locator, timeout=10)
            captcha_btn.click()
            print("Captcha detectado y clickeado con éxito.")
        except Exception as e:
            print(f"El captcha no apareció o hubo un error: {e}")

        self.driver.quit()