from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):
    # locators
    TITLE = (By.CLASS_NAME, "title")  # e.g. "Products"
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    # check whether the page is loaded via title, return True or False
    def is_loaded(self):
        return "Products" in self.get_text(self.TITLE)

    # click "Add to cart" for the backpack
    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    # get the number of items added into the cart
    def get_cart_num(self):
        return int(self.get_text(self.CART_BADGE))

    # click cart icon to go to cart page
    def go_to_cart_page(self):
        self.click(self.CART_ICON)
