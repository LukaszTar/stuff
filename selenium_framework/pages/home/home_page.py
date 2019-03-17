from base.selenium_driver import SeleniumDriver


class HomePage(SeleniumDriver):
    """Page class for www.x-kom.pl home page"""

    _login_icon = "//div[contains(@class,'hover-active')]"
    _login_link = "//a[@href='https://www.x-kom.pl/logowanie']"
    _register_link = "//a[@href='https://www.x-kom.pl/rejestracja/']"
    _user_icon = "//i[contains(@class,'icon-user')]"
    _logout_button = "//a[@href='/wyloguj']"
    _home_page_url = "https://www.x-kom.pl/"

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def hover_to_login_icon(self):
        self.mouse_hover(self._login_icon, locator_type='xpath')

    def click_on_login_link(self):
        self.element_click(self._login_link, locator_type='xpath')

    def click_on_register_link(self):
        self.wait_for_element_to_be_clicable(self._register_link, locator_type='xpath')
        self.element_click(self._register_link, locator_type='xpath')

    def hover_to_user_icon(self):
        self.mouse_hover(self._user_icon, locator_type='xpath')

    def verify_user_icon_presence(self):
        user_icon_present = self.is_element_present(self._user_icon, locator_type='xpath')
        print(user_icon_present)
        assert user_icon_present==True

    def click_on_logout_button(self):
        self.element_click(self._logout_button, locator_type='xpath')

    def logout(self):
        self.hover_to_user_icon()
        self.click_on_logout_button()

    def go_to_home_page(self):
        self.go_to_page(self._home_page_url)

    def go_to_register_page(self):
        self.hover_to_login_icon()
        self.click_on_register_link()
