from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
    
    def element_click(self, locator='', locator_type='id', element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locator_type)
            print_stack()

    def send_enter(self, locator='', locator_type='id', element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.send_keys(Keys.ENTER)
            self.log.info("ENTER send to element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("ENTER not send to element with locator: " + locator +
                          " locatorType: " + locator_type)

    def element_send_keys(self, data, locator='', locator_type='id', element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locator_type)
            print_stack()

    def is_element_present(self, locator='', locator_type='id', element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locator_type)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locator_type)
                return False
        except:
            print("Element not found")
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

    def wait_for_element_to_be_visible(self, locator, locator_type="id",
                         timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be visible")

            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
            print_stack()
        return element

    def get_element_list(self, locator, locator_type="id"):
        """
        NEW METHOD
        Get list of elements
        """
        element = None
        try:
            locator_type = locator_type.lower()
            byType = self.get_by_type(locator_type)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        return element

    def get_text(self, locator="", locatorType="id", element=None, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.get_element(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def is_element_displayed(self, locator="", locator_type="id", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        is_displayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            return is_displayed
        except:
            print("Element not found")
            return False

    def web_scroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def switch_to_frame(self, locator=''):
        try:
            self.driver.switch_to.frame(locator)
            self.log.info("Switched to frame with locator: " + locator)
        except:
            self.log.info("Cannot switched to frame with locator: " + locator)

    def switch_to_default_frame(self):
        try:
            self.driver.switch_to.default_content()
            self.log.info("Switched to default frame")
        except:
            self.log.info("Cannot switched to default frame")

    def previous_page(self):
        try:
            self.driver.back()
            self.log.info('Navigated one page back')
        except:
            self.log.info('Could not navigate one page back')


