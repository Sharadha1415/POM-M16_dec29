import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver            ## self.driver --> setup --> driver --> webdriver.Chrome()
        self.wait = WebDriverWait(driver, 30)

    def enter_email(self):
        self.driver.find_element("id", "Email").send_keys('abcdefgh@gmail.com')

    def enter_password(self):
        self.driver.find_element("id", "Password").send_keys("123456789")

    def click_login_btn(self):
        self.driver.find_element("css selector", 'input[value="Log in"]').click()
        time.sleep(2)

    def verify_unsuccessfull_login(self):
        self.wait.until(EC.visibility_of_element_located(('xpath', '//span[contains(text(), "Login was unsuccessful")]')))


