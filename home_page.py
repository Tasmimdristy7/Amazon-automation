from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.amazon.com/")

    def search_product(self, product_name):
        self.input_text(By.ID, "twotabsearchtextbox", product_name)
        self.click(By.ID, "nav-search-submit-button")
