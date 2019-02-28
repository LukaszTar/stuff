from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    _login_icon = "//div[@class='name']"
    _login_link = "//a[@href='https://www.x-kom.pl/logowanie']"
    _username_textbox = "login"
    _password = "password"
    _login_button = "//button[@type='submit']"
    _user_icon = "//i[contains(@class,'icon-user')]"
    _empty_username_info = "login-error"
    _empty_password_info = "password-error"
    _logout_button = "//a[@href='/wyloguj']"

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def hover_to_login_icon(self):
        self.mouse_hover(self._login_icon, locator_type='xpath')

    def hover_to_user_icon(self):
        self.mouse_hover(self._user_icon, locator_type='xpath')

    def click_on_logout_button(self):
        self.element_click(self._logout_button, locator_type='xpath')

    def click_on_login_link(self):
        self.element_click(self._login_link, locator_type='xpath')

    def enter_username(self, username):
        self.element_send_keys(username, self._username_textbox, locator_type='name')

    def enter_password(self, password):
        self.element_send_keys(password, self._password, locator_type='name')

    def click_on_login_button(self):
        self.element_click(self._login_button, locator_type='xpath')

    def verify_user_icon_presence(self):
        user_icon_present = self.is_element_present(self._user_icon, locator_type='xpath')
        print(user_icon_present)
        assert user_icon_present==True

    def verify_empty_username_info(self):
        user_icon_present = self.is_element_present(self._empty_username_info, locator_type='id')
        assert user_icon_present==True

    def verify_empty_password_info(self):
        user_icon_present = self.is_element_present(self._empty_password_info, locator_type='id')
        assert user_icon_present==True

    def verify_empty_credentials_info(self):
        self.verify_empty_username_info()
        self.verify_empty_password_info()

    def login(self, username='', password=''):
        self.hover_to_login_icon()
        self.click_on_login_link()
        self.enter_username(username)
        self.enter_password(password)
        self.click_on_login_button()

    def logout(self):
        self.hover_to_user_icon()
        self.click_on_logout_button()

