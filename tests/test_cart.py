import unittest
from selenium import webdriver
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from pages.cart_page import CartPage


class TestCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        #input("Press Enter to close the browser...")
        self.driver.quit()

    def test01_remove_from_cart(self):
        # login successfully
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        # product page
        product_page = ProductsPage(self.driver)
        product_page.add_backpack_to_cart()
        product_page.go_to_cart_page()

        # cart page
        cart_page = CartPage(self.driver)
        cart_badge_num = int(cart_page.get_num_of_cart_badge())
        cart_page.remove_backpack()

        # check whether the item is present or not, since for SauceDemo, same item cannot be added to the cart twice
        self.assertFalse(cart_page.is_backpack_in_cart())

        # check the number of cart badge to double verify
        self.assertEqual(cart_badge_num - 1, cart_page.get_num_of_cart_badge())
        print(" Backpack removed and number of cart is correct")

    def test02_continue_shopping(self):
        # login successfully
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        # product page
        product_page = ProductsPage(self.driver)
        product_page.go_to_cart_page()

        # cart page
        cart_page = CartPage(self.driver)
        cart_page.continue_shopping()

        self.assertIn("inventory.html", self.driver.current_url)  # check whether go back to product page
        print("Continue shopping went back to product page successfully.")

    def test03_checkout_page(self):
        # login successfully
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        # product page
        product_page = ProductsPage(self.driver)
        product_page.add_backpack_to_cart()
        product_page.go_to_cart_page()

        # cart page
        cart_page = CartPage(self.driver)
        cart_page.checkout()

        self.assertIn("checkout-step-one.html", self.driver.current_url)  # check whether go to checkout page
        print("Checkout page loaded successfully.")


if __name__ == "__main__":
    unittest.main()
