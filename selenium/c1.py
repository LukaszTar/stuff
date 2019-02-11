import selenium
from selenium import webdriver

class FFBrowserTest:
    def __init__(self):
        self.driver = webdriver.Firefox()
    def open_page(self, page):
        self.driver.get(page)
    def find_elem(self):
        try:
            found_element = self.driver.find_elements_by_class_name('inputs')
            for elem in found_element:
                elem.send_keys('Element test')
        except selenium.common.exceptions.NoSuchElementException as e:
            print(getattr(e, 'msg'))
    def close_page(self):
        self.driver.close()
test = FFBrowserTest()
test.open_page('https://learn.letskodeit.com/p/practice')
test .find_elem()

#test.close_page()