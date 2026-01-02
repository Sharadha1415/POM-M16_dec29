import time

from object_repository.cartpage_loc import CartPageLocators
from generic_utilities.webdriver_utility import WebDriverUtility

cart_loc = CartPageLocators()

class CartPage:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> setup --> driver
        self.util = WebDriverUtility(driver)

    def select_country(self, country):
        self.util.select_option_by_text(cart_loc.country_id, country)
        time.sleep(1)

    def click_terms_service(self):
        self.util.click_on_element(cart_loc.terms_service)
        time.sleep(2)

    def click_checkout(self):
        self.util.click_on_element(cart_loc.checkout)







