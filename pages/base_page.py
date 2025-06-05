'''
Reusable helper class for all pages:
Element finding, click action, text input and reading text content.
'''

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    # accept driver and store as self.driver
    def __init__(self, driver):
        self.driver = driver

    # wait and find the element with locator tuple(By.ID, value) and return it
    # if not show up in 10 seconds, throw error
    def find_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise Exception(f"Timeout. Element {locator} not found within {timeout} seconds.")

    # find and click locator element
    def click(self, locator):
        self.find_element(locator).click()

    # find and send text to it
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    # find and get locator's text
    def get_text(self, locator):
        return self.find_element(locator).text




