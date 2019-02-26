from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.status import Status
from ddt import ddt, data, unpack
import unittest
import pytest
import time


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    @data(('JavaScript for beginners', '5169606510095854', '1220', '234', '90241'),
          ('Selenium WebDriver With Java', '5169606510095854', '1220', '234', '90241'))
    @unpack
    def test_invalid_enrollment(self, course_name, cc_num, cc_exp, cc_cvv, postal):
        self.courses.enter_course_name(course_name)
        time.sleep(2)
        self.courses.select_course_to_enroll(course_name)
        self.courses.enroll_course(cc_num, cc_exp, cc_cvv, postal)
        status = self.courses.verify_enroll_failed()
        self.ts.mark_final('ENROLLMENT_VERIFICATION', status, '## ENROLLMENT_VERIFICATION ##')
        self.courses.go_to_previous_page()
        self.courses.click_all_courses_link()
