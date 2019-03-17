from base.selenium_driver import SeleniumDriver
from utitilies.status import Status
import re


class RegisterPage(SeleniumDriver):
    """Page class for www.x-kom.pl register page"""

    _name_testbox = 'firstName'
    _empty_name_message = "//span[contains(text(), 'Podaj imię.')]"
    _last_name_testbox = 'lastName'
    _empty_last_name_message = "//span[contains(text(), 'Podaj nazwisko.')]"
    _email_textbox = 'email'
    _empty_email_message = "//span[contains(text(), 'Podaj adres e-mail.')]"
    _incorrect_email_address = "//span[contains(text(), 'Podaj prawidłowy adres e-mail.')]"
    _too_short_password_message = "//span[contains(text(), 'Hasło powinno mieć minimum 6 znaków.')]"
    _password_textbox = 'password'
    _empty_password_message = "//span[contains(text(), 'Podaj hasło.')]"
    _register_button = "//button[@type='submit']"
    _empty_terms_checkbox = "//span[contains(text(), 'Zaakceptuj regulamin.')]"
    _accept_terms_checkbox = "termsOfUseAcceptation"
    _marked_invalid_textbox = "div[contains(@class, 'invalid')]"
    _marked_valid_textbox = "div[@class='marked valid']"

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.st = Status(driver)

    def enter_name(self, name):
        self.element_send_keys(name, self._name_testbox, locator_type='id')

    def enter_last_name(self, last_name):
        self.element_send_keys(last_name, self._last_name_testbox, locator_type='id')

    def enter_password(self, password):
        self.element_send_keys(password, self._password_textbox, locator_type='id')

    def enter_email(self, email):
        self.element_send_keys(email, self._email_textbox, locator_type='id')

    def accept_terms_checkbox(self):
        self.element_click(self._accept_terms_checkbox, locator_type='id')

    def click_on_register_button(self):
        self.element_click(self._register_button, locator_type='xpath')

    def verify_form_fields(self, name='', last_name='', password='', email='', accept_terms='no'):
        self.verify_name(name)
        self.verify_last_name(last_name)
        self.verify_email(email)
        self.verify_password(password)
        self.verify_accept_terms(accept_terms)

    def fill_register_form(self, name='', last_name='', password='', email='', accept_terms='no'):
        if accept_terms == 'yes':
            self.accept_terms_checkbox()
        self.enter_name(name)
        self.enter_last_name(last_name)
        self.enter_password(password)
        self.enter_email(email)

    def register(self, name='', last_name='', password='', email='', accept_terms='no'):
        self.fill_register_form(name, last_name, password, email, accept_terms)
        self.click_on_register_button()
        self.verify_form_fields(name, last_name, password, email, accept_terms)
        return self.st

    def verify_name(self, name):
        if name:
            result = re.search("^[a-zA-ZęóąśłżźćńĘÓĄŚŁŻŹĆŃ_\\- ]*$", name)
            print(result)
            if result:
                return self.verify_valid_form(self._empty_name_message)
            else:
                return self.verify_invalid_form(self._empty_name_message)
        else:
            return self.verify_invalid_form(self._empty_name_message)

    def verify_last_name(self, last_name):
        if last_name:
            result = re.search("^[a-zA-ZęóąśłżźćńĘÓĄŚŁŻŹĆŃ_\\- ]*$", last_name)
            print(result)
            if result:
                return self.verify_valid_form(self._empty_last_name_message)
            else:
                return self.verify_invalid_form(self._empty_last_name_message)
        else:
            return self.verify_invalid_form(self._empty_last_name_message)

    def verify_email(self, email):
        if email:
            result = re.search('^[_a-z0-9-]+(\\.[_a-z0-9-]+)*@[a-z0-9-]+(\\.[a-z0-9-]+)*(\\.[a-z]{2,4})$', email)
            if result:
                return self.verify_valid_form(self._empty_email_message)
            else:
                return self.verify_invalid_form(self._incorrect_email_address)
        else:
            return self.verify_invalid_form(self._empty_email_message)

    def verify_password(self, password):
        if password:
            if len(password)<6:
                return self.verify_invalid_form(self._too_short_password_message)
            else:
                return self.verify_valid_form(self._empty_password_message)
        else:
            return self.verify_invalid_form(self._empty_password_message)

    def verify_accept_terms(self, accept_terms):
        if accept_terms=='yes':
            return self.verify_valid_form(self._empty_terms_checkbox)
        else:
            return self.verify_invalid_form(self._empty_terms_checkbox)

    def verify_invalid_form(self, locator):
        empty_form_message_exists = self.is_element_visible(locator, locator_type='xpath')
        return empty_form_message_exists

    def verify_valid_form(self, locator):
        incorrect_form_message = self.is_element_visible(locator, locator_type='xpath')
        return not incorrect_form_message

    def clear_form(self, locator):
        self.clear_textbox(locator, locator_type='id')

    def clear_register_form(self):
        self.clear_form(self._name_testbox)
        self.clear_form(self._last_name_testbox)
        self.clear_form(self._email_textbox)
        self.clear_form(self._password_textbox)
