from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class WaitWrapper:

    def __init__(self, driver):
        self.driver = driver
        self.wait_for_search_results = WebDriverWait(
            self.driver, timeout=20)

    def wait_for_element(self, locator, locator_id=By.XPATH):

        element = self.wait_for_search_results.until(EC.presence_of_element_located((locator_id, locator)))
        return element


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

        search_button = self.driver.find_element(By.XPATH, "//button[contains(@class,'bpk-button-2YQI1')]")
        search_button.click()

        ww = WaitWrapper(self.driver)
        ww.wait_for_element("(//*[@class='fqs-best-icon'])")

        select_flight = self.driver.find_element(
            By.XPATH, "(//div[@class='CTASection__cta-section-p4bPE']/button[contains(@class,'bpk-button')])")
        select_flight.click()

    def close_window(self):
        self.driver.close()


test = FindFlight()
test.find()
time.sleep(5)
test.close_window()
