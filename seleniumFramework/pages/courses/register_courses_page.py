import utilities.custom_logger as cl
from base.basepage import BasePage


class RegisterCoursesPage(BasePage):

    log = cl.customLogger()
    _search_box = 'search-courses'
    _course_list = "//div[contains(@class, 'course-listing-title')]"
    _course = "//div[contains(text(), '{0}') and contains(@class, 'course-listing-title')]"
    _all_courses_link = "//a[contains(text(), 'All Courses') and contains(@class, 'fedora-navbar-link')]"
    _enroll_button = 'enroll-button-top'
    _cc_num = 'cardnumber'
    _cc_exp = 'exp-date'
    _cc_cvv = 'cvc'
    _cc_postal = 'postal'
    _terms = 'agreed_to_terms_checkbox'
    _submit_enroll = 'confirm-purchase'
    _enroll_error_message = 'cc__error'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_course_name(self, course_name):
        self.wait_for_element(self._search_box)
        self.element_send_keys(course_name, self._search_box)
        self.send_enter(self._search_box)

    def select_course_to_enroll(self, course_name):
        self.wait_for_element_to_be_visible(self._course.format(course_name), locator_type='xpath')
        self.element_click(self._course.format(course_name), locator_type='xpath')

    def enter_enroll_in_course(self):
        self.element_click(self._enroll_button)

    def enter_card_number(self, num):
        self.switch_to_frame(locator='__privateStripeFrame4')
        self.element_send_keys(num, self._cc_num, locator_type='name')
        self.switch_to_default_frame()

    def enter_card_exp(self, exp):
        self.switch_to_frame(locator='__privateStripeFrame5')
        self.element_send_keys(exp, self._cc_exp, locator_type='name')
        self.switch_to_default_frame()

    def enter_card_cvv(self, cvv):
        self.switch_to_frame(locator='__privateStripeFrame6')
        self.element_send_keys(cvv, self._cc_cvv, locator_type='name')
        self.switch_to_default_frame()

    def enter_postal(self, postal):
        self.switch_to_frame(locator='__privateStripeFrame7')
        self.element_send_keys(postal, self._cc_postal, locator_type='name')
        self.switch_to_default_frame()

    def get_number_of_elements(self):
        return len(self.get_element_list(self._course_list, locator_type='xpath'))

    def click_i_agree(self):
        self.element_click(self._terms)

    def click_enroll_submitt_button(self):
        self.element_click(self._submit_enroll)

    def click_all_courses_link(self):
        self.element_click(self._all_courses_link, locator_type='xpath')

    def enter_credit_card_information(self, num, exp, cvv, postal):
        self.enter_card_number(num)
        self.enter_card_exp(exp)
        self.enter_card_cvv(cvv)
        self.enter_postal(postal)
        self.click_i_agree()

    def go_to_previous_page(self):
        self.previous_page()

    def enroll_course(self, num='', exp='', cvv='', postal=''):
        self.enter_enroll_in_course()
        self.web_scroll(direction='down')
        self.enter_credit_card_information(num, exp, cvv, postal)
        self.click_enroll_submitt_button()

    def verify_enroll_failed(self):
        self.wait_for_element_to_be_visible(self._enroll_error_message, locator_type='class')
        enroll_status = self.is_element_displayed(self._enroll_error_message, locator_type='class')
        return enroll_status
