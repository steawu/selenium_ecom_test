from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # step one locators
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    CANCEL = (By.ID, "cancel")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    # step two page locators
    FINISH = (By.ID, "finish")
    COMPLETE = (By.CSS_SELECTOR, "[data-test='complete-header']")

    # filling required info to step two
    def fill_checkout(self, first_name, last_name, zip):
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.ZIP, zip)
        self.click(self.CONTINUE)

    # cancel
    def cancel(self):
        self.click(self.CANCEL)

    # continue to step twp
    def conti_checkout(self):
        self.click(self.CONTINUE)

    # click finish button to complete
    def finish_checkout(self):
        self.click(self.FINISH)

    # get complete order message
    def thanks_msg(self):
        return self.get_text(self.COMPLETE)

    def error_message(self):
        return self.get_text(self.ERROR)

    def total_price(self):
        prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        total_price = 0
        for price in prices:
            price_text = price.text.replace("$", "")
            total_price += float(price_text)
        return total_price


