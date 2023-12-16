from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_product_page(self, product_index=1):
        product_xpath = f"(//div[@data-index='{product_index}']//h2)[1]//a"
        self.click(By.XPATH, product_xpath)
