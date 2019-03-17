import pytest
import unittest
from pages.login.login_page import LoginPage
from pages.home.home_page import HomePage


@pytest.mark.usefixtures('class_level_fixture')
class TestLoginPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def custom_setup(self):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

    @pytest.mark.run(order=1)
    def test_valid_login(self):
        self.lp.login(username='testuser@email.com', password='abcabc')
        self.hp.verify_user_icon_presence()
        self.hp.logout()

    @pytest.mark.run(order=5)
    def test_invalid_login(self):
        self.lp.login(username='testuser@email.pl', password='abc')
        self.lp.verify_incorrect_credentials_info()
        self.lp.go_to_previous_page()

    @pytest.mark.run(order=2)
    def test_empty_login_credentials(self):
        self.lp.login()
        self.lp.verify_empty_credentials_info()
        self.lp.go_to_previous_page()

    @pytest.mark.run(order=3)
    def test_empty_username_login(self):
        self.lp.login(password='abcabc')
        self.lp.verify_empty_username_info()
        self.lp.go_to_previous_page()

    @pytest.mark.run(order=4)
    def test_empty_password_login(self):
        self.lp.login(username='testuser@email.pl')
        self.lp.verify_empty_password_info()
        self.lp.go_to_previous_page()
