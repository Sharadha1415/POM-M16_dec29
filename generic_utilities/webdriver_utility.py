from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class WebDriverUtility:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.ac = ActionChains(driver)

    def click_on_element(self, var_name):
        self.driver.find_element(*var_name).click()

    def enter_data(self, var_name, value):
        self.driver.find_element(*var_name).send_keys(value)

    def select_option_by_text(self, var_name, text):
        listbox = self.driver.find_element(*var_name)
        select_obj = Select(listbox)
        select_obj.select_by_visible_text(text)

    def ele_visibility(self, ele):
        self.wait.until(EC.visibility_of_element_located(ele))

    def hover(self, var_name):
        ele = self.driver.find_element(*var_name)
        self.ac.move_to_element(ele).perform()

    def pagedown(self):
        self.ac.send_keys(Keys.PAGE_DOWN).perform()



























