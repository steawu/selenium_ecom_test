import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium import webdriver
from pages.login_page import LoginPage


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    # run after each test to close
    def tearDown(self):
        #input("Press Enter to close the browser...")
        self.driver.quit()

    # login with correct username & password
    def test01_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user","secret_sauce")
        self.assertIn("inventory.html", self.driver.current_url)    # if login success, will jump to inventory page
        print("Login successfully.")

    # test with locked_out_user as username to get specific error message
    def test02_locked_user(self):
        login_page = LoginPage(self.driver)
        login_page.login("locked_out_user", "secret_sauce")
        self.assertIn("Epic sadface: Sorry, this user has been locked out",
                      login_page.get_error_text())
        print("Login test with locked username passed.")
