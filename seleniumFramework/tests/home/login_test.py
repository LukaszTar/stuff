from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest


class LoginTest(unittest.TestCase):

    # def __init__(self):
    #     self.base_url = 'https://letskodeit.teachable.com/'

    def test_valid_credentials(self):
        base_url = 'https://letskodeit.teachable.com/'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)

        lt = LoginPage(driver)
        lt.login('test@email.com', 'abcabc')
        user_icon = driver.find_element(By. XPATH, "//img[@class='gravatar']")

        if user_icon is not None:
            print('Login successful')
        else:
            print('Login not successful')
