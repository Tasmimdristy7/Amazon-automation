from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def input_text(self, by, value, text):
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        element.clear()
        element.send_keys(text)

    def get_text(self, by, value):
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        return element.text

