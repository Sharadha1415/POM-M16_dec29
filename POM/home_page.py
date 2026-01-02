import time

from object_repository.homepage_loc import HomePageLocators
from generic_utilities.webdriver_utility import WebDriverUtility

home_loc = HomePageLocators()

class HomePage:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> setup --> driver = webdriver.Chrome()
        self.util = WebDriverUtility(driver)

    def click_login_link(self):
        self.util.click_on_element(home_loc.login_link)
        time.sleep(2)

    def verify_successfull_login(self):
        self.util.ele_visibility(home_loc.logout_link)
        time.sleep(2)

    def hover_to_computers(self):
        self.util.hover(home_loc.computers)
        time.sleep(1)

    def click_on_desktop(self):
        self.util.click_on_element(home_loc.desktops)
        time.sleep(2)









