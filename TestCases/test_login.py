import time
import pytest
from Utilities.Logger_utitlity import logger_class
from Utilities.read_config_utility import ReadConfig_class

class Test_Login01:
    base_url = ReadConfig_class.base_url()
    log = logger_class.log_gen_method()
    driver = None

    def test_bankapp_url_001(self,driver_setup):
        self.driver=driver_setup
        self.log.info("Testcase test_bankapp_url_001 is started")
        self.log.info(f"Opening the Bank Application URL-->{self.base_url} ")
        self.driver.get(self.base_url)
        # Initialize the test case
        self.log.info(f"Checking the Bank Application Title-->{self.driver.title}")
        if self.driver.title == "Bank Application":
            print("Test Case Passed: Bank Application URL Opened")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("..\\Screenshots\\Base_url_pass.png")
            time.sleep(3)
            self.log.info("Testcase test_bankapp_url_001 is passed\n")
            assert True
        else:
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("..\\Screenshots\\Base_url_fail.png")
            print("Test Case Failed: Bank Application URL Not Opened")
            self.log.info("Testcase test_bankapp_url_001 is failed\n")
            assert False
