from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = 'commit'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # def get_login_link(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def get_email_field(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def get_password_field(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def get_login_button(self):
    #     return self.driver.find_element(By.NAME, self._login_button)

    def click_login_link(self):
        self.element_click(self._login_link, locator_type='link')

    def type_email_field(self, user_name):
        self.element_send_keys(user_name, self._email_field, locator_type='id')

    def type_password(self, password):
        self.element_send_keys(password, self._password_field, locator_type='id')

    def click_login_button(self):
        self.element_click(self._login_button, locator_type='name')

    def login(self, user_name, password):
        self.click_login_link()
        self.type_email_field(user_name)
        self.type_password(password)
        self.click_login_button()

