import time

from object_repository.simpcomp_page_loc import SimpCompPageLocators

simpcomp_loc = SimpCompPageLocators()

class SimpleComputerPage:

    def __init__(self, driver):
        self.driver = driver

    def select_processor(self):
        self.driver.find_element(*simpcomp_loc.processor).click()
        time.sleep(1)

    def add_to_cart(self):
        self.driver.find_element(*simpcomp_loc.add_to_cart_btn).click()
        time.sleep(2)

    def close_noti(self):
        self.driver.find_element(*simpcomp_loc.close).click()
        time.sleep(2)

    def click_shopping_cart(self):
        self.driver.find_element(*simpcomp_loc.shopping_cart).click()
        time.sleep(2)

    









