from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    # locators
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CONTINUE_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT = (By.ID, "checkout")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    PRODUCT_NAME = (By.CLASS_NAME,"inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK_BUTTON)

    def continue_shopping(self):
        self.click(self.CONTINUE_BUTTON)

    def checkout(self):
        self.click(self.CHECKOUT)

    def get_num_of_cart_badge(self):
        try:
            return int(self.get_text(self.CART_BADGE))
        except Exception:
            return 0       # if badge is gone, means 0 items in the cart

    # check backpack is appear in cart or not
    def is_backpack_in_cart(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")  # all products list in carts
        return any("Backpack" in item.text for item in items)


