from POM.homepage import HomePage
from POM.loginpage import LoginPage


def test_unsuccessfull_login(setup):
    home = HomePage(setup)      ## HomePage(driver)
    log = LoginPage(setup)
    home.click_login_link()
    log.enter_email()
    log.enter_password()
    log.click_login_btn()
    log.verify_unsuccessfull_login()




























