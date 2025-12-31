import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from object_repository.loginpage_loc import LoginPageLocators

login_loc = LoginPageLocators()


class LoginPage:

    def __init__(self, driver):
        self.driver = driver            ## self.driver --> setup --> driver --> webdriver.Chrome()
        self.wait = WebDriverWait(driver, 30)

    def enter_email(self, email_id):
        self.driver.find_element(*login_loc.email_txtbox).send_keys(email_id)

    def enter_password(self, password):
        self.driver.find_element(*login_loc.pwd_txtbox).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*login_loc.login_btn).click()
        time.sleep(2)

    def verify_unsuccessfull_login(self):
        self.wait.until(EC.visibility_of_element_located(login_loc.unsuccessfull_msg))


