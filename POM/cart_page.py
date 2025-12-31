import time
from selenium.webdriver.support.select import Select

from object_repository.cartpage_loc import CartPageLocators

cart_loc = CartPageLocators()

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def select_country(self, country):
        country_name = self.driver.find_element(*cart_loc.country_id)
        select_country = Select(country_name)
        select_country.select_by_visible_text(country)
        time.sleep(1)

    def click_terms_service(self):
        self.driver.find_element(*cart_loc.terms_service).click()
        time.sleep(2)

    def click_checkout(self):
        self.driver.find_element(*cart_loc.checkout).click()







