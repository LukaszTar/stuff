from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time


class WaitWrapper:

    def __init__(self, driver):
        self.driver = driver
        self.wait_for_search_results = WebDriverWait(
            self.driver, timeout=60)

    def wait_for_element(self, locator, locator_id=By.XPATH):
        try:
            element = self.wait_for_search_results.until(EC.presence_of_element_located((locator_id, locator)))
            return element
        except TimeoutException:
            print('Element not found')


class FindFlight:

    def __init__(self):

        profile = FirefoxProfile()
        profile.set_preference('browser.formfill.enable', False)
        self.driver = webdriver.Firefox(profile)

    def find(self):
        url = 'https://www.skyscanner.pl'
        self.driver.maximize_window()
        self.driver.get(url)

        home_textbox = self.driver.find_element_by_id('fsc-origin-search')
        home_textbox.send_keys(Keys.CONTROL + 'a')
        home_textbox.send_keys(Keys.DELETE)
        home_textbox.send_keys('Poznan')

        destination_textbox = self.driver.find_element_by_id('fsc-destination-search')
        destination_textbox.send_keys('Sydney (SYD)')

        depart_date_button = self.driver.find_element(By.XPATH,
                                                      "//*[@class='form-item-2Br2r form-item-oneline-3vFjh'][1]/button")
        depart_date_button.click()

        depart_date_calander = self.driver.find_element(By.XPATH, "//span[text()='12']/parent::button")
        depart_date_calander.click()

        return_date_button = self.driver.find_element(By.XPATH,
                                                      "//*[@class='form-item-2Br2r form-item-oneline-3vFjh'][2]/button")
        return_date_button.click()

        return_date_calander = self.driver.find_element(By.XPATH, "//span[text()='24']/parent::button")
        return_date_calander.click()

        search_button = self.driver.find_element(By.XPATH, "//button[contains(@class,'bpk-button-2YQI1')]")
        search_button.click()

        ww = WaitWrapper(self.driver)
        ww.wait_for_element("(//*[@class='fqs-best-help'])")

        select_flight = self.driver.find_element(
            By.XPATH, "(//div[@class='CTASection__cta-section-p4bPE']/button[contains(@class,'bpk-button')])")
        select_flight.click()
        self.driver.save_screenshot('D:\\userdata\\targonsk\\Desktop\\screenshot.png')

    def new_window(self):
        url = 'https://learn.letskodeit.com/p/practice'
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id('openwindow').click()

        parent_window = self.driver.current_window_handle

        handles = self.driver.window_handles

        for handle in handles:
            if handle is not parent_window:
                self.driver.switch_to.window(handle)
        self.driver.maximize_window()

    def close_window(self):
        self.driver.quit()


test = FindFlight()
test.new_window()
time.sleep(5)
test.close_window()
