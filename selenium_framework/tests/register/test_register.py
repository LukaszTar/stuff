from pages.home.home_page import HomePage
from pages.register.register_page import RegisterPage
from utitilies.read_csv import read_data_from_csv
from utitilies.status import Status
from ddt import ddt, data, unpack
import unittest
import pytest


@pytest.mark.usefixtures('class_level_fixture')
@ddt
class TestRegister(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def custom_setup(self):
        self.rp = RegisterPage(self.driver)
        self.hp = HomePage(self.driver)
        self.st = Status(self.driver)
        yield
        self.rp.clear_register_form()

    @pytest.mark.run(order=2)
    @data(*read_data_from_csv('incorrect_name_data.csv'))
    @unpack
    def test_invalid_name_form(self, name, last_name, password, email, accept_terms):
        self.hp.go_to_register_page()
        self.rp.fill_register_form(name, last_name, password, email, accept_terms)
        self.rp.click_on_register_button()
        name_textbox_status = self.rp.verify_name(name)
        self.st.mark(name_textbox_status, 'Verify_textbox_for_Imie'.format(name))
        self.st.mark_final(
            'test_invalid_register_empty_form name:{}, last_name:{}, password:{}, email:{}, accept_terms:{}\n\n'.format(name, last_name, password, email, accept_terms))

    @pytest.mark.run(order=1)
    @data(*read_data_from_csv('incorrect_last_name_data.csv'))
    @unpack
    def test_invalid_last_name_form(self, name, last_name, password, email, accept_terms):
        self.hp.go_to_register_page()
        self.rp.fill_register_form(name, last_name, password, email, accept_terms)
        self.rp.click_on_register_button()
        last_name_status = self.rp.verify_last_name(last_name)
        self.st.mark(last_name_status, 'Verify_textbox_for_Nazwisko'.format(last_name))
        self.st.mark_final(
            'test_invalid_register_empty_form name:{}, last_name:{}, password:{}, email:{}, accept_terms:{}\n\n'.format(name, last_name, password, email, accept_terms))

    @pytest.mark.run(order=3)
    @data(*read_data_from_csv('incorrect_email_data.csv'))
    @unpack
    def test_invalid_email_form(self, name, last_name, password, email, accept_terms):
        self.hp.go_to_register_page()
        self.rp.fill_register_form(name, last_name, password, email, accept_terms)
        self.rp.click_on_register_button()
        email_status = self.rp.verify_email(email)
        self.st.mark(email_status, 'Verify_textbox_for_Adres_e-mail'.format(email))
        self.st.mark_final(
            'test_invalid_register_empty_form name:{}, last_name:{}, password:{}, email:{}, accept_terms:{}\n\n'.format(name, last_name, password, email, accept_terms))

    @pytest.mark.run(order=4)
    @data(*read_data_from_csv('incorrect_password_data.csv'))
    @unpack
    def test_invalid_password_form(self, name, last_name, password, email, accept_terms):
        self.hp.go_to_register_page()
        self.rp.fill_register_form(name, last_name, password, email, accept_terms)
        self.rp.click_on_register_button()
        password_status = self.rp.verify_password(password)
        self.st.mark(password_status, 'Verify_textbox_for_Haslo'.format(password))
        self.st.mark_final(
            'test_invalid_register_empty_form name:{}, last_name:{}, password:{}, email:{}, accept_terms:{}\n\n'.format(name, last_name, password, email, accept_terms))

    @pytest.mark.run(order=5)
    @data(*read_data_from_csv('incorrect_terms_data.csv'))
    @unpack
    def test_invalid_terms_checkbox(self, name, last_name, password, email, accept_terms):
        self.hp.go_to_register_page()
        self.rp.fill_register_form(name, last_name, password, email, accept_terms)
        self.rp.click_on_register_button()
        accept_terms_status = self.rp.verify_accept_terms(accept_terms)
        self.st.mark(accept_terms_status, 'Verify_textbox_for_accept_terms'.format(accept_terms))
        self.st.mark_final(
            'test_invalid_register_empty_form name:{}, last_name:{}, password:{}, email:{}, accept_terms:{}\n\n'.format(name, last_name, password, email, accept_terms))
