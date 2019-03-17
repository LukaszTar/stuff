from base.selenium_driver import SeleniumDriver
from pages.home.home_page import HomePage


class LoginPage(SeleniumDriver):
    """Page class for www.x-kom.pl login page"""

    _username = "login"
    _password = "password"
    _login_button = "//button[@type='submit']"
    _empty_username_info = "login-error"
    _empty_password_info = "password-error"
    _register_button = "//a[@href='/rejestracja/']"
    _incorrect_credentials_info = "//div[contains(@class,'alert-dismissible') and contains(@class, 'alert-warning')]"

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.hp = HomePage(driver)

    def click_on_register_buton(self):
        self.element_click(self._register_button, locator_type='xpath')

    def enter_username(self, username):
        self.element_send_keys(username, self._username, locator_type='name')

    def enter_password(self, password):
        self.element_send_keys(password, self._password, locator_type='name')

    def click_on_login_button(self):
        self.element_click(self._login_button, locator_type='xpath')

    def verify_empty_username_info(self):
        user_icon_present = self.is_element_present(self._empty_username_info, locator_type='id')
        assert user_icon_present==True

    def verify_empty_password_info(self):
        user_icon_present = self.is_element_present(self._empty_password_info, locator_type='id')
        assert user_icon_present==True,'Cannot locate user icon'

    def verify_empty_credentials_info(self):
        self.verify_empty_username_info()
        self.verify_empty_password_info()

    def verify_incorrect_credentials_info(self):
        incorrect_credentials_info_present = self.is_element_present(self._incorrect_credentials_info, locator_type='xpath')
        assert incorrect_credentials_info_present==True

    def login(self, username='', password=''):
        self.hp.hover_to_login_icon()
        self.hp.click_on_login_link()
        self.enter_username(username)
        self.enter_password(password)
        self.click_on_login_button()
