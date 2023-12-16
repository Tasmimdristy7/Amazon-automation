from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_subtotal(self):
        return self.get_text(By.ID, "sc-subtotal-amount-activecart")
