from base.basepage import BasePage


class Navigate(BasePage):

    _my_courses = "//a[contains(@text(), 'My Courses')]"
    _all_courses = "//a[contains(@text(), 'All Courses')]"
    _practice = "//a[contains(@text(), 'Practice')]"
    _user_icon = "//a[contains(@class, 'fedora-navbar-link') and contains(@class, 'dropdown-toggle')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_my_courses(self):
        self.element_click(self._my_courses, locator_type='xpath')

    def navigate_to_all_courses(self):
        self.element_click(self._all_courses, locator_type='xpath')

    def navigate_to_practice(self):
        self.element_click(self._practice, locator_type='xpath')

    def navigate_to_user_icon(self):
        self.element_click(self._user_icon, locator_type='xpath')
