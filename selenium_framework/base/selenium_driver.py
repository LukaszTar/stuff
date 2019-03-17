from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotSelectableException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from utitilies.custom_logger import custom_logger
from datetime import datetime
import os


class SeleniumDriver:
    """Wrapper class for selenium"""

    log = custom_logger()

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type.lower() == 'id':
            return By.ID
        elif locator_type.lower() == 'xpath':
            return By.XPATH
        elif locator_type.lower() == 'name':
            return By.NAME
        elif locator_type.lower() == 'class':
            return By.CLASS_NAME
        elif locator_type.lower() == 'link':
            return By.LINK_TEXT
        elif locator_type.lower() == 'css':
            return By.CSS_SELECTOR
        elif locator_type.lower() == 'partial_link':
            return By.PARTIAL_LINK_TEXT
        elif locator_type.lower() == 'tag':
            return By.TAG_NAME
        else:
            self.log.info('Incorrect locator type: {}'.format(locator_type))
        return False

    def get_element(self, locator, locator_type='id'):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info('Element found with locator: {} and locator type: {}'.format(locator, locator_type))
            return element
        except:
            self.log.info('Element not found with locator: {} and locator type: {}'.format(locator, locator_type))
            return element

    def mouse_hover(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            self.log.info('Mouseover to element with locator: {} and locator type: {}'.format(locator, locator_type))
            action.reset_actions()
        except:
            self.log.info('Could not mouseover to element with locator: {} and locator type: {}'.format(locator, locator_type))

    def element_click(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info('Clicked on element with locator: {} and locator type: {}'.format(locator, locator_type))
        except Exception as e:
            self.log.info(str(e) + ' Cannot click on element with locator: {} and locator type: {}'.format(locator, locator_type))

    def element_send_keys(self, data, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            for char in data:
                element.send_keys(char)
            self.log.info('Keys {} send to element with locator: {} and locator type: {}'.format(data, locator, locator_type))
        except:
            self.log.info('Keys {} not send to element with locator: {} and locator type: {}'.format(data, locator, locator_type))

    def element_send_enter(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(Keys.ENTER)
            self.log.info('Enter key send to element with locator: {} and locator type: {}'.format(locator, locator_type))
        except:
            self.log.info('Enter key not send to element with locator: {} and locator type: {}'.format(locator, locator_type))

    def is_element_present(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element with locator: {} and locator type: {} found".format(locator, locator_type))
                return True
            else:
                self.log.info("Element with locator: {} and locator type: {} not found".format(locator, locator_type))
                return False
        except:
            self.log.info("Element with locator: {} and locator type: {} not found".format(locator, locator_type))
            return False

    def is_element_visible(self, locator, locator_type='id'):
        element = self.get_element(locator, locator_type)
        if element is not None:
            element_is_visible = element.is_displayed()
            if element_is_visible:
                self.log.info("Element with locator: {} and locator type: {} visible".format(locator, locator_type))
                return True
            else:
                self.log.info("Element with locator: {} and locator type: {} not visible".format(locator, locator_type))
                return False
        else:
            return False

    def wait_for_element_to_be_clicable(self, locator, locator_type='id', timeout=2, poll_frequency=0.1):
        element = None
        try:
            by_type = self.get_by_type(locator_type=locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[ElementNotSelectableException, ElementNotInteractableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.info('Element with locator: {} and locator type: {} is clicable'.format(locator, locator_type))
        except:
            self.log.info('Element with locator: {} and locator type: {} is not clicable'.format(locator, locator_type))
        return element

    def go_to_page(self, url):
        try:
            self.driver.get(url)
            self.log.info('Went to page: {}'.format(url))
        except:
            self.log.info('Page: {} could not be opened'.format(url))

    def go_to_previous_page(self):
        try:
            self.driver.back()
            self.log.info('Went to previous page')
        except:
            self.log.info('Could not navigate to previous page')

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

    def clear_textbox(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.clear()
        except:
            self.log.info('Could not clear element with locator:{} and locator type:{}'.format(locator, locator_type))


