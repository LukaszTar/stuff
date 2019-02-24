"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver


class Status(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(Status, self).__init__(driver)
        self.resultList = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: " + result_message)
                else:
                    self.resultList.append("FAIL")
                    self.log.info("### VERIFICATION FAILED :: " + result_message)
                    self.save_screenshots(result_message)
            else:
                self.resultList.append("FAIL")
                self.log.info("### VERIFICATION FAILED :: " + result_message)
                self.save_screenshots(result_message)
        except:
            self.resultList.append("FAIL")
            self.log.info("### Exception Occurred !!!")
            self.save_screenshots(result_message)

    def mark(self, result, result_message):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.set_result(result, result_message)
        if 'FAIL' in self.resultList:
            self.log.error(test_name + ' ### VERIFICATION FAILED ' + result_message)
            self.resultList.clear()
            assert 0
        else:
            self.log.info(test_name + ' ### VERIFICATION PASSED ' + result_message)
            self.resultList.clear()
