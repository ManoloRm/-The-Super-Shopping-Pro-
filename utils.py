from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
def click_when_ready(driver, locator, timeout=10):
    """Espera a que un elemento sea clickeable y le da clic."""
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
    element.click()

import random
import string
def generate_random_email(domain="test.com"):
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"user_{random_str}@{domain}"
def geneate_random_password():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def switch_to_iframe(driver, locator, timeout=10):

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    wait = WebDriverWait(driver, timeout)
    wait.until(EC.frame_to_be_available_and_switch_to_it(locator))