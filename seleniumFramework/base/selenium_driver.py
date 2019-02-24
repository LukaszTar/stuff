from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from traceback import print_stack
from datetime import datetime
import logging
import os
from utilities.custom_logger import customLogger as cl


class SeleniumDriver:

    log = cl(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def save_screenshots(self, result_message):
        file_name = str(datetime.now().strftime(result_message + '.' + '%Y%m%dT%H:%M:%S:%f')) + '.png'
        relative_file_path = os.path.join('../screenshots/', file_name)
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, relative_file_path)
        screenshots_dir = os.path.join(current_dir, '../screenshots/')
        try:
            if not os.path.exists(screenshots_dir):
                os.mkdir(screenshots_dir)
            self.driver.save_screenshot(file_path)
            self.log.info('Screenshot: ' + file_path + ' saved')
        except:
            self.log.error('Could not save screenshot under: ' + screenshots_dir)

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type + " not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            byType = self.get_by_type(locator_type)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator " + locator + " locatorType: " + locator_type)
        except:
            self.log.info("Element not Found with locator " + locator + " locatorType: " + locator_type)
        return element
    
    def element_click(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info('Clicked on locator: ' + locator + ' locatorType ' + locator_type)
        except:
            self.log.error('cannot click on locator: ' + locator + ' locatorType ' + locator_type)

    def element_send_keys(self, data, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info('data send to locator: ' + locator + ' locatorType ' + locator_type)
        except:
            self.log.error('data not send to locator: ' + locator + ' locatorType ' + locator_type)
            print_stack()

    def is_element_present(self, locator, locator_type):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                self.wait_for_element(locator, locator_type)
                self.log.info("Element found with locator " + locator + " locatorType: " + locator_type)
                return True
            else:
                self.log.info("Element not Found with locator " + locator + " locatorType: " + locator_type)
                return False
        except:
            self.log.info("Element not Found with locator " + locator + " locatorType: " + locator_type)
            return False

    def wait_for_element(self, locator, locator_type="id",
                         timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
            print_stack()
        return element
