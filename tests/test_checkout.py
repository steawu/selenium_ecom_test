import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        #input("Press Enter to close the browser...")
        self.driver.quit()

    # helper method for add one a backpack to cart: login -> product -> cart pages
    def login_product_cart(self):
        # login
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        # product page to add item to cart
        product_page = ProductsPage(self.driver)
        product_page.add_backpack_to_cart()
        product_page.go_to_cart_page()

        # cart page to check out then
        cart_page = CartPage(self.driver)
        cart_page.checkout()

    def test01_successfully_checkout(self):
        self.login_product_cart()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_checkout("abc", "abc", "123456")
        checkout_page.finish_checkout()

        # check whether jump to complete page
        self.assertIn("checkout-complete.html", self.driver.current_url)
        #self.assertIn("Thanks you", checkout_page.thanks_msg())
        print("Successfully checkout.")

    def test02_missing_first_name(self):
        self.login_product_cart()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_checkout("", "abc", "123456")
        checkout_page.conti_checkout()

        error = checkout_page.error_message()
        print(error)
        self.assertIn("First Name is required", error)
        print("Missing first name.")

    def test03_missing_last_name(self):
        self.login_product_cart()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_checkout("abc", "", "123456")
        checkout_page.conti_checkout()

        error = checkout_page.error_message()
        self.assertIn("Last Name is required", error)
        print("Missing last name.")

    def test04_missing_zip(self):
        self.login_product_cart()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_checkout("abc", "abc", "")
        checkout_page.conti_checkout()

        error = checkout_page.error_message()
        self.assertIn("Postal Code is required", error)
        print("Missing postal code.")

    # for step one, cancel button will jump back to cart page
    def test05_cancel_checkout_step_one(self):
        self.login_product_cart()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.cancel()

        self.assertIn("cart.html", self.driver.current_url)
        print("Back to cart page successfully.")

    # for step two, cancel button will jump back to product page
    def test06_cancel_checkout_step_two(self):
        self.login_product_cart()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_checkout("abc", "abc", "123456")
        checkout_page.cancel()

        #print("test", self.driver.current_url)
        self.assertIn("inventory.html", self.driver.current_url)
        print("Back to product page successfully.")

    def test07_total_price(self):
        self.login_product_cart()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_checkout("abc", "abc", "123456")

        item_total_text = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
        item_total = float(item_total_text.replace("Item total: $", ""))
        self.assertEqual(checkout_page.total_price(), item_total)
        print("Total price is correct.")














