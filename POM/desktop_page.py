import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from object_repository.desktop_page_loc import DesktopLocators

desktop_loc = DesktopLocators()

class DesktopPage:

    def __init__(self, driver):
        self.driver = driver
        self.ac = ActionChains(driver)

    def sort(self, text):
        sort_by = self.driver.find_element(*desktop_loc.sort_drpdwn)
        select_sortby = Select(sort_by)
        select_sortby.select_by_visible_text(text)
        time.sleep(2)

    def view(self, text):
        view_as = self.driver.find_element(*desktop_loc.view_drpdwn)
        select_viewas = Select(view_as)
        select_viewas.select_by_visible_text(text)
        time.sleep(2)

    def scroll_page_by(self):
        self.ac.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)

    def click_simple_com(self):
        self.driver.find_element(*desktop_loc.simp_comp).click()
        time.sleep(2)

















