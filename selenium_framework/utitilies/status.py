from base.selenium_driver import SeleniumDriver


class Status(SeleniumDriver):

    def __init__(self, driver):
        super(Status, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message):
        """Saves the status of each test and continue even if test is failed"""

        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL ### " + result_message)
                else:
                    self.result_list.append("FAIL")
                    self.log.error("### VERIFICATION FAILED ### " + result_message)
                    self.save_screenshots(result_message)
            else:
                self.result_list.append("FAIL")
                self.log.error("### VERIFICATION FAILED ### " + result_message)
                self.save_screenshots(result_message)
        except:
            self.result_list.append("FAIL")
            self.log.error("### Exception Occurred !!! ###")
            self.save_screenshots(result_message)

    def mark(self, result, result_message):
        self.set_result(result, result_message)

    def mark_final(self, test_name):
        """Marks the final status of the test"""

        if "FAIL" in self.result_list:
            self.log.error('### VERIFICATION FAILED ### ' + test_name)
            self.result_list.clear()
            assert 0
        else:
            self.log.info('### VERIFICATION PASSED ### ' + test_name)
            self.result_list.clear()
