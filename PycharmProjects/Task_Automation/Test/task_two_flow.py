## Imports for system configuration ###
import os
import sys
sys.path.append(os.path.abspath('../'))
### Imports from selenium ###
from selenium import webdriver
from Locators_Amazon.Locators import Locators
from Pages_Amazon.user import User
import time

### Imports for unittest to specify test case and to report Generation ####

import unittest
import HtmlTestRunner


class TestTwo(unittest.TestCase):

    #### chrome driver initalization inside the method ####
    @classmethod
    def setUpClass(cls):

        root_path = os.path.expanduser('~').replace("\\", "/")
        chrome_path = root_path + '/PycharmProjects/Task_Automation/drivers/chromedriver.exe'
        cls.driver = webdriver.Chrome(executable_path=chrome_path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    '''
    Test Case Flow for Clear Trip.
    '''

    @classmethod
    def test_two_flow(self):

        # driver = ;
        self.driver.get("https://www.amazon.in")

        ### Created an object for class User ###

        am_user = User(self.driver)
        # am_user = User()
        # am_user.print_user()
        am_user.enter_search_text(search_text=Locators.keyword_search)
        am_user.select_from_search_type_dropdown(drop_value="book")
        am_user.click_on_go()
        time.sleep(5)
        am_user.filter_by_format_type(format_type="paperback")
        time.sleep(3)
        am_user.select_offers_link_in_product()
        min_value = am_user.select_from_list_of_book()
        am_user.select_add_to_cart(rupees=min_value)
        time.sleep(4)
        am_user.click_proceed_to_checkout()
        time.sleep(3)
        am_user.login_into_amazon(user_name=Locators.user_name, password=Locators.password)

        details = {"f_name": "MuthuNathan", "mobile": 8903413339, "pin": "560079",
        "address": "krishnamoorthi layour 2nd cross tavarekere", "landmark": "Near muthoot fincorp",
        "city": "Bangalore", "state": "Karnataka"}

        am_user.enter_address_details(details=details)
        am_user.click_on_continue_button()
        time.sleep(4)
        am_user.click_on_deliver_to_address()
        time.sleep(3)
        am_user.click_order_placement()
        time.sleep(3)

    #### Closing chrome driver after completion of test case ####

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    root_path = os.path.expanduser('~').replace("\\", "/")
    report_path = root_path + '/PycharmProjects/Task_Automation/reports'
    print(report_path, "Report_Path")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=report_path))
