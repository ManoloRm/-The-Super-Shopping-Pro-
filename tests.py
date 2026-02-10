import utils
import selenium
import time
from utils import wait_for_element
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
        pages.login.passwordBox(self, test_pass).send_keys(Keys.ENTER)
        time.sleep(2)
        pages.login.signin_button(self).click()
        try:
            from utils import switch_to_iframe
            switch_to_iframe(self.driver, (By.TAG_NAME, "iframe"))
            captcha_canvas = self.driver.find_element(By.CSS_SELECTOR, "canvas")
            if captcha_canvas.is_displayed():
                print("✅ Captcha detectado con éxito.")
            self.driver.switch_to.default_content()

        except Exception as e:
            print(f"❌ El captcha no apareció o el selector falló: {e}")
            self.driver.switch_to.default_content()  # Aseguramos salir del frame pase lo que pase
        self.driver.quit()