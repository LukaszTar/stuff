from selenium import webdriver
import os


class DriverFactory:

    def __init__(self, browser):
        """Initialize DriverFactory class"""
        self.browser = browser

    def initialize_driver(self):
        """Get WebDriver instance based on the browser

        Returns:
            WebDriver instance
        """
        base_url = 'https://www.x-kom.pl/'

        if self.browser.lower() == 'firefox':
            driver = webdriver.Firefox()
        elif self.browser.lower() == 'chrome':
            chrome_driver = '../config_files/chromedriver.exe'
            os.environ['chromedriver.chrome.driver'] = chrome_driver
            driver = webdriver.Chrome(chrome_driver)
        elif self.browser.lower() == 'ie':
            driver = webdriver.Ie()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(base_url)

        return driver
