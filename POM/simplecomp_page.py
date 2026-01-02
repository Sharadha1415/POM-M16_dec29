import time

from object_repository.simpcomp_page_loc import SimpCompPageLocators
from generic_utilities.webdriver_utility import WebDriverUtility

simpcomp_loc = SimpCompPageLocators()

class SimpleComputerPage:

    def __init__(self, driver):
        self.driver = driver
        self.util = WebDriverUtility(driver)

    def select_processor(self):
        self.util.click_on_element(simpcomp_loc.processor)
        time.sleep(1)

    def add_to_cart(self):
        self.util.click_on_element(simpcomp_loc.add_to_cart_btn)
        time.sleep(2)

    def close_noti(self):
        self.util.click_on_element(simpcomp_loc.close)
        time.sleep(2)

    def click_shopping_cart(self):
        self.util.click_on_element(simpcomp_loc.shopping_cart)
        time.sleep(2)

    









