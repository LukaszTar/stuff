from pages.home.navigation_page import Navigate
from utilities.custom_logger import customLogger as cl
from base.basepage import BasePage
import logging


class LoginPage(BasePage):

    log = cl(logging.DEBUG)
    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = 'commit'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = Navigate(driver)

    def click_login_link(self):
        self.element_click(self._login_link, locator_type='link')

    def type_email_field(self, user_name):
        self.element_send_keys(user_name, self._email_field, locator_type='id')

    def type_password(self, password):
        self.element_send_keys(password, self._password_field, locator_type='id')

    def click_login_button(self):
        self.element_click(self._login_button, locator_type='name')

    def login(self, user_name='', password=''):
        self.click_login_link()
        self.type_email_field(user_name)
        self.type_password(password)
        self.click_login_button()

    def verify_successful_login(self):
        user_avatar_present = self.is_element_present("//img[@class='gravatar']", locator_type='xpath')

        return user_avatar_present

    def verify_login_failed(self):
        invalid_credential_message_presence = self.is_element_present(
            "//div[contains(text(),'Invalid email or password.')]", locator_type='xpath')
        return invalid_credential_message_presence

    def verify_title(self):
        return self.verifyPageTitle("Let's Kode It")

    def logout(self):
        self.nav.navigate_to_user_icon()
        self.element_click("//a[@href='/sign_out']", locator_type='xpath')
