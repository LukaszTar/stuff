from pages.home.login_page import LoginPage
from utilities.status import Status
import pytest
import unittest


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, oneTimeSetUp):
        self.lt = LoginPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_credentials(self):
        self.lt.login('test@email.com', 'abcabc')
        result1 = self.lt.verify_title()
        self.ts.mark(result1, 'TITLE VERIFICATION')
        result2 = self.lt.verify_successful_login()
        self.ts.mark_final('LOGIN VERIFICATION', result2, '## LOGIN VERIFICATION ##')

    @pytest.mark.run(order=1)
    def test_invalid_credentials(self):
        self.lt.logout()
        self.lt.login()
        result = self.lt.verify_login_failed()
        self.ts.mark_final('INVALID LOGIN', result, '## INVALID LOGIN VERIFICATION ##')
