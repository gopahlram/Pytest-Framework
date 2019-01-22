from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from Locators_Amazon.Locators import Locators


class AddressPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_address_details(self, details=None):
        '''
        :param details: {"f_name":"", "mobile": , "pin": ,
        "address":"", "landmark":"", "city":"", "state":""}
        :return:
        '''

        try:
            self.driver.find_element(By.XPATH, Locators.full_name).clear()
            self.driver.find_element(By.XPATH, Locators.full_name).send_keys(details["f_name"])

            self.driver.find_element(By.XPATH, Locators.mob_num).clear()
            self.driver.find_element(By.XPATH, Locators.mob_num).send_keys(details["mobile"])

            self.driver.find_element(By.XPATH, Locators.pincode).clear()
            self.driver.find_element(By.XPATH, Locators.pincode).send_keys(details["pin"])

            self.driver.find_element(By.XPATH, Locators.address_one).clear()
            self.driver.find_element(By.XPATH, Locators.address_one).send_keys(details["address"])

            self.driver.find_element(By.XPATH, Locators.landmark).clear()
            self.driver.find_element(By.XPATH, Locators.landmark).send_keys(details["landmark"])
            #
            # self.driver.find_element(By.XPATH, Locators.city).send_keys(details["city"])
            #
            # self.driver.find_element(By.XPATH, Locators.state).clear()
            # self.driver.find_element(By.XPATH, Locators.state).send_keys(details["state"])

        finally:
            pass

    def select_address_type(self, address_type=None):

        try:
            option = {"home": Locators.RES, "res": Locators.COM}
            if address_type in option:
                address_type = option[address_type]
            a_ele = Select(self.driver.find_element(By.XPATH, Locators.select_add_type))
            a_ele.select_by_value(address_type)
        finally:
            pass

    def click_on_continue_button(self):

        try:
            ac = ActionChains(self.driver)
            ac.move_to_element(self.driver.find_element(By.XPATH, Locators.continue_button))
            ac.click(self.driver.find_element(By.XPATH, Locators.continue_button))
            ac.perform()
        finally:
            pass

    def click_on_deliver_to_address(self):

        try:
            ele = '//input[@value="Deliver to this address"]'
            if self.driver.find_elements(By.XPATH, ele):
                ac = ActionChains(self.driver)
                ac.move_to_element(self.driver.find_element(By.XPATH, ele))
                ac.click(self.driver.find_element(By.XPATH, ele))
                ac.perform()
            else:
                pass
        finally:
            pass

    def click_order_placement(self):

        try:
            a = self.driver.find_elements(By.XPATH, Locators.click_order_continue)
            ac = ActionChains(self.driver)
            ac.move_to_element(a[1])
            ac.click(a[1])
            ac.perform()
        finally:
            pass

