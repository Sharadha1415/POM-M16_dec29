import time

from object_repository.loginpage_loc import LoginPageLocators
from generic_utilities.webdriver_utility import WebDriverUtility

login_loc = LoginPageLocators()

class LoginPage:

    def __init__(self, driver):
        self.driver = driver            ## self.driver --> setup --> driver --> webdriver.Chrome()
        self.util = WebDriverUtility(driver)

    def enter_email(self, email_id):
        self.util.enter_data(login_loc.email_txtbox, email_id)

    def enter_password(self, password):
        self.util.enter_data(login_loc.pwd_txtbox, password)

    def click_login_btn(self):
        self.util.click_on_element(login_loc.login_btn)
        time.sleep(2)

    def verify_unsuccessfull_login(self):
        self.util.ele_visibility(login_loc.unsuccessfull_msg)


