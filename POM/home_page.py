import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> setup --> driver = webdriver.Chrome()
        self.wait = WebDriverWait(driver, 10)
        self.ac = ActionChains(driver)

    def click_login_link(self):
        self.driver.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(2)

    def verify_successfull_login(self):
        self.wait.until(EC.visibility_of_element_located(('xpath', '//a[text()="Log out"]')))
        time.sleep(2)

    def hover_to_computers(self):
        computers = self.driver.find_element('xpath', '//a[contains(text(), "Computers")]')
        self.ac.move_to_element(computers).perform()
        time.sleep(1)

    def click_on_desktop(self):
        self.driver.find_element('xpath', '//a[contains(text(), "Desktops")]').click()
        time.sleep(2)































