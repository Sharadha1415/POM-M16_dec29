import time

class SimpleComputerPage:

    def __init__(self, driver):
        self.driver = driver

    def select_processor(self):
        self.driver.find_element('xpath', '//input[@id="product_attribute_75_5_31_96"]').click()
        time.sleep(1)

    def add_to_cart(self):
        self.driver.find_element('xpath', '//input[@id="add-to-cart-button-75"]').click()
        time.sleep(2)

    def close_noti(self):
        self.driver.find_element('xpath', '//span[@class="close"]').click()
        time.sleep(2)

    def click_shopping_cart(self):
        self.driver.find_element("xpath", '//span[text()="Shopping cart"]').click()
        time.sleep(2)

    









