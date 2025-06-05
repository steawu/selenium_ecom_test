import unittest
from selenium import webdriver
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.product_page import ProductsPage


class TestProductsPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    # run after each test
    def tearDown(self):
        #input("Press Enter to close the browser...")
        self.driver.quit()

    # check whether product page loaded after correct login
    def test01_product_page_loads(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(self.driver)
        self.assertTrue(products_page.is_loaded())
        print("Product page loaded successfully.")

    # add a backpack to shopping cart and check the number of items of cart badge
    def test02_add_to_cart(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(self.driver)
        products_page.add_backpack_to_cart()

        num = products_page.get_cart_num()
        self.assertEqual(num, 1)
        print("Added to cart successfully.")


if __name__ == "__main__":
    unittest.main()
