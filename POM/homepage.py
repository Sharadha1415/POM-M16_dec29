import time

class HomePage:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> setup --> driver = webdriver.Chrome()

    def click_login_link(self):
        self.driver.find_element("xpath", '//a[text()="Log in"]').click()
        time.sleep(2)






























