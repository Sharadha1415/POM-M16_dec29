from POM.home_page import HomePage
from POM.login_page import LoginPage
from POM.desktop_page import DesktopPage
from POM.simplecomp_page import SimpleComputerPage
from POM.cart_page import CartPage

from generic_utilities.excel_utility import read_excel

path = r'C:\Users\Ramya\PycharmProjects\POM-M16-Dec26-2025\external_files\testdata.xlsx'
data = read_excel(path, 'data')
print(data)


def test_unsuccessfull_login(setup):
    home = HomePage(setup)      ## HomePage(driver)
    log = LoginPage(setup)
    home.click_login_link()
    log.enter_email(data['invalid_email'])
    log.enter_password(data['invalid_pwd'])
    log.click_login_btn()
    log.verify_unsuccessfull_login()


def test_checkout(setup):
    home = HomePage(setup)
    log = LoginPage(setup)
    desktop = DesktopPage(setup)
    simp = SimpleComputerPage(setup)
    cart = CartPage(setup)

    home.click_login_link()
    log.enter_email(data['valid_email'])
    log.enter_password(data['valid_pwd'])
    log.click_login_btn()
    home.verify_successfull_login()
    home.hover_to_computers()
    home.click_on_desktop()
    desktop.sort(data['sort_data'])
    desktop.view(data['view_data'])
    desktop.scroll_page_by()
    desktop.click_simple_com()
    simp.select_processor()
    simp.add_to_cart()
    simp.close_noti()
    simp.click_shopping_cart()
    cart.select_country()
    cart.click_terms_service()
    cart.click_checkout()
























