from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from traceback import print_stack


class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

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
            print("Locator type " + locator_type + " not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            byType = self.get_by_type(locator_type)
            element = self.driver.find_element(byType, locator)
            print("Element Found")
        except:
            print("Element not found")
        return element
    
    def element_click(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            print('Clicked on locator: ' + locator + 'locatorType' + locator_type)
        except:
            print('cannot click on locator: ' + locator + 'locatorType' + locator_type)
            print_stack()

    def element_send_keys(self, data, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            print('data send to locator: ' + locator + 'locatorType' + locator_type)
        except:
            print('data not send to locator: ' + locator + 'locatorType' + locator_type)
            print_stack()
        
    def wait_for_element(self, locator, locator_type="id",
                         timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.get_by_type(locator_type)
            print("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element