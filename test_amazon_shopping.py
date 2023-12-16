import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.LoggerUtil import LoggerUtil
from config.AppConfig import AppConfig

class TestAmazonShopping(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = LoggerUtil.get_logger(cls.__name__)
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_search_and_add_to_cart(self):
        # Test Case 1: Search for a laptop, add to cart, and verify subtotal
        home_page = HomePage(self.driver)
        home_page.search_product("laptop")

        search_results_page = SearchResultsPage(self.driver)
        search_results_page.open_product_page()

        product_page = ProductPage(self.driver)
        product_page.add_to_cart()

        cart_page = CartPage(self.driver)
        subtotal = cart_page.get_cart_subtotal()
        self.logger.info(f"Test Case 1 - Cart subtotal for laptop: {subtotal}")
        self.assertTrue(subtotal)

    def test_add_multiple_items_to_cart(self):
        # Test Case 2: Add multiple items to the cart and verify the count
        home_page = HomePage(self.driver)
        home_page.search_product("smartphone")

        search_results_page = SearchResultsPage(self.driver)
        search_results_page.open_product_page()

        product_page = ProductPage(self.driver)
        product_page.add_to_cart()

        # Go back to search results and add another item
        self.driver.back()
        search_results_page.open_product_page(product_index=2)
        product_page.add_to_cart()

        cart_page = CartPage(self.driver)
        item_count = cart_page.get_cart_item_count()
        self.logger.info(f"Test Case 2 - Cart item count: {item_count}")
        self.assertEqual(item_count, 2)

    def test_search_invalid_product(self):
        # Test Case 3: Search for an invalid product and verify no results found
        home_page = HomePage(self.driver)
        home_page.search_product("invalid_product")

        search_results_page = SearchResultsPage(self.driver)
        no_results_message = search_results_page.get_no_results_message()
        self.logger.info(f"Test Case 3 - No results message: {no_results_message}")
        self.assertIn("No results found", no_results_message)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
