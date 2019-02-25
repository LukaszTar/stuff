import utilities.custom_logger as cl
from selenium.webdriver.common.keys import Keys
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger()
    _search_box = 'search-courses'
    _course = 'course-listing-title'
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

    def select_course_to_enroll(self):
        self.wait_for_element(self._course, locator_type='class')
        self.element_click(self._course, locator_type='class')

    def enter_enroll_in_course(self):
        self.element_click(self._enroll_button)

    def enter_card_number(self, num):
        self.element_send_keys(num, self._cc_num, locator_type='name')

    def enter_card_exp(self, exp):
        self.element_send_keys(exp, self._cc_exp, locator_type='name')

    def enter_card_cvv(self, cvv):
        self.element_send_keys(cvv, self._cc_cvv, locator_type='name')

    def enter_postal(self, postal):
        self.element_send_keys(postal, self._cc_postal, locator_type='name')

    def click_i_agree(self):
        self.element_click(self._terms)

    def click_enroll_submitt_button(self):
        self.element_click(self._submit_enroll)

    def enter_credit_card_information(self, num, exp, cvv, postal):
        self.switch_to_frame(locator='__privateStripeFrame4')
        #self.wait_for_element(self._cc_num, locator_type='name')
        self.enter_card_number(num)
        self.switch_to_default_frame()
        self.switch_to_frame(locator='__privateStripeFrame5')
        self.enter_card_exp(exp)
        self.switch_to_default_frame()
        self.switch_to_frame(locator='__privateStripeFrame6')
        self.enter_card_cvv(cvv)
        self.switch_to_default_frame()
        self.switch_to_frame(locator='__privateStripeFrame7')
        self.enter_postal(postal)
        self.switch_to_default_frame()
        self.click_i_agree()

    def enroll_course(self, num='', exp='', cvv='', postal=''):
        self.enter_enroll_in_course()
        self.web_scroll(direction='down')
        self.enter_credit_card_information(num, exp, cvv, postal)
        self.click_enroll_submitt_button()

    def verify_enroll_failed(self):
        self.wait_for_element_to_be_visible(self._enroll_error_message, locator_type='class')
        enroll_status = self.is_element_displayed(self._enroll_error_message, locator_type='class')
        return enroll_status