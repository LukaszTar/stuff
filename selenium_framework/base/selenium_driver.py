from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class SeleniumDriver:
    """Wrapper class for selenium"""

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_by_type(locator_type):
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
            print('Incorrect locator type')
        return False

    def get_element(self, locator, locator_type='id'):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            print('Element found with locator: {} and locator type: {}'.format(locator, locator_type))
            return element
        except:
            print('Element not found with locator: {} and locator type: {}'.format(locator, locator_type))
            return element

    def mouse_hover(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            print('Mouseover to element with locator: {} and locator type: {}'.format(locator, locator_type))
        except:
            print('Could not mouseover to element with locator: {} and locator type: {}'.format(locator, locator_type))

    def element_click(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            print('Clicked on element with locator: {} and locator type: {}'.format(locator, locator_type))
        except:
            print('Cannot click on element with locator: {} and locator type: {}'.format(locator, locator_type))

    def element_send_keys(self, data, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            for char in data:
                element.send_keys(char)
            print('Keys {} send to element with locator: {} and locator type: {}'.format(data, locator, locator_type))
        except:
            print('Keys {} not send to element with locator: {} and locator type: {}'.format(data, locator, locator_type))
    
    def is_element_present(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                print("Element with locator: {} and locator type: {} found".format(locator, locator_type))
                return True
            else:
                print("Element with locator: {} and locator type: {} not found".format(locator, locator_type))
                return False
        except:
            print("Element with locator: {} and locator type: {} not found".format(locator, locator_type))
            return False

    def go_to_previous_page(self):
        try:
            self.driver.back()
            print('Went to previous page')
        except:
            print('Could not navigate to previous page')



