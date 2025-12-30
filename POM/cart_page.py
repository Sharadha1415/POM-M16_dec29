import time
from selenium.webdriver.support.select import Select

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def select_country(self):
        country = self.driver.find_element('xpath', '//select[@id="CountryId"]')
        select_country = Select(country)
        select_country.select_by_visible_text("India")
        time.sleep(1)

    def click_terms_service(self):
        self.driver.find_element('css selector', 'input[id="termsofservice"]').click()
        time.sleep(2)

    def click_checkout(self):
        self.driver.find_element('xpath', '//button[@id="checkout"]').click()







