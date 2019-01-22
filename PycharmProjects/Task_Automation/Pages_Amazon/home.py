from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from Locators_Amazon.Locators import Locators
import time


class Home:

    def _init_(self, driver):
        self.driver = driver

    def enter_search_text(self, search_text=None):
        '''
        :param search_text:  "search keyword"
        :return:
        '''
        try:
            self.driver.find_element(By.XPATH, Locators.search_field).send_keys(search_text)
        finally:
            pass

    def select_from_search_type_dropdown(self, drop_value=None):
        '''
        :param drop_value:  "values of drop down"
        :return:
        '''

        try:
            option = {"book":Locators.books_value}
            if drop_value in option:
                drop_value = option[drop_value]
            a_select = Select(self.driver.find_element(By.XPATH, Locators.search_dropdown))
            a_select.select_by_value(drop_value)
        finally:
            pass

    def click_on_go(self):

        try:
            ac = ActionChains(self.driver)
            ac.move_to_element(self.driver.find_element(By.XPATH, Locators.search_button))
            ac.click(self.driver.find_element(By.XPATH, Locators.search_button))
            ac.perform()
            time.sleep(5)
        finally:
            pass

    def click_proceed_to_checkout(self):

        try:
            ac = ActionChains(self.driver)
            ac.move_to_element(self.driver.find_element(By.XPATH,Locators.proceed_to_checkout))
            ac.click(self.driver.find_element(By.XPATH,Locators.proceed_to_checkout))
            ac.perform()
        finally:
            pass
