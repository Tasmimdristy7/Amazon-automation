from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_to_cart(self):
        self.click(By.ID, "add-to-cart-button")
