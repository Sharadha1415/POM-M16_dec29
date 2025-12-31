class LoginPageLocators:
    email_txtbox = "id", "Email"
    pwd_txtbox = "id", "Password"
    login_btn = "css selector", 'input[value="Log in"]'
    unsuccessfull_msg = 'xpath', '//span[contains(text(), "Login was unsuccessful")]'
