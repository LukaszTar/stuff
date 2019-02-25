from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_invalid_enrollment(self):
        self.courses.enter_course_name('JavaScript')
        self.courses.select_course_to_enroll()
        self.courses.enroll_course('5169606510095854', '1220', '234', '90241')
        status = self.courses.verify_enroll_failed()
        print(status)
        self.ts.mark_final('ENROLLMENT_VERIFICATION', status, '## ENROLLMENT_VERIFICATION ##')
