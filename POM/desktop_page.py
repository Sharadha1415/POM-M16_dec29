import time

from object_repository.desktop_page_loc import DesktopLocators
from generic_utilities.webdriver_utility import WebDriverUtility

desktop_loc = DesktopLocators()

class DesktopPage:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> setup --> driver
        self.util = WebDriverUtility(driver)

    def sort(self, text):
        self.util.select_option_by_text(desktop_loc.sort_drpdwn, text)

    def view(self, text):
        self.util.select_option_by_text(desktop_loc.view_drpdwn, text)

    def scroll_page_by(self):
        self.util.pagedown()
        time.sleep(2)

    def click_simple_com(self):
        self.util.click_on_element(desktop_loc.simp_comp)
        time.sleep(2)

















