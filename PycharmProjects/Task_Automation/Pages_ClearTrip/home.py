'''
Methods in Home Page
'''


import time
from datetime import datetime, timedelta
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Locators.locators import Locators


class Home:

    def _init_(self, driver):
        self.driver = driver

    def click_on_login_button(self):

        try:

            ac = ActionChains(self.driver)
            ac.move_to_element(self.driver.find_element(By.XPATH, Locators.your_trips))
            ac.click(self.driver.find_element(By.XPATH, Locators.your_trips))
            ac.perform()

            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, Locators.sign_in)),"SignIn button not visible")

            # time.sleep(5)
            ace = ActionChains(self.driver)
            ace.move_to_element(self.driver.find_element(By.XPATH, Locators.sign_in))
            ace.click(self.driver.find_element(By.XPATH, Locators.sign_in))
            ace.perform()


        finally:
            pass

    def select_trip_type(self, trip_type=None):

        '''
        trip_type = "one"/"round"/"multiple"
        '''

        try:
            option = {"one":"OneWay","round":"RoundTrip","multiple":"MultiCity"}
            ele_trip = self.driver.find_element(By.XPATH,Locators.click_on_round_trip.format(option[trip_type]))
            if trip_type in option:
                if ele_trip.is_selected():

                    print("User already selected the option '{0}'".format(trip_type))
                else:
                    self.driver.find_element(By.XPATH, Locators.click_on_round_trip.format(option[trip_type])).click()
        finally:
            pass

    def enter_travel_details(self, From_=None, To_=None):
        """
        From_ = "delhi" / user destination
        To_  = "bglr"  / user destination
        """

        try:
            option = {"bangalore": "BLR", "delhi": "DEL"}

            if From_ in option:
                self.driver.find_element(By.XPATH, Locators.From_txt_field).clear()
                self.driver.find_element(By.XPATH, Locators.From_txt_field).send_keys(option[From_])
                # self.driver.find_element(By.XPATH, Locators.From_txt_field).send_keys(Keys.SPACE)
                time.sleep(5)
                self.driver.find_element(By.XPATH, Locators.From_txt_field).send_keys(Keys.ENTER)

            if To_ in option:
                self.driver.find_element(By.XPATH, Locators.To_txt_field).clear()
                self.driver.find_element(By.XPATH, Locators.To_txt_field).send_keys(option[To_])
                # self.driver.find_element(By.XPATH, Locators.To_txt_field).send_keys(Keys.SPACE)
                time.sleep(5)
                self.driver.find_element(By.XPATH, Locators.To_txt_field).send_keys(Keys.ENTER)
        finally:
            pass

    def select_calender(self, for_=None, day=None, month=None, year=None):

        '''
        for_ = "depart" / "return_date"
        '''

        try:
            if for_=="depart":
                self.driver.find_element(By.XPATH,Locators.depart_on_icon).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH,Locators.to_select_date.format(month,year,day)).click()
            elif for_=="return_date":
                self.driver.find_element(By.XPATH,Locators.return_on_icon).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH,Locators.to_select_date.format(month,year,day)).click()
        finally:
            pass

    def enter_passenger_details(self,passenger_type=None,number_of_passenger=None):

        '''
        :param passenger_type:  "adult" / 'child' / 'infant'
        :param number_of_passenger:
        '''

        try:

            if passenger_type == "adult":
                a_ele = Select(self.driver.find_element(By.XPATH, Locators.select_adults))
            elif passenger_type == "child":
                a_ele = Select(self.driver.find_element(By.XPATH, Locators.select_children))
            elif passenger_type == "infant":
                pass

            a_ele.select_by_value(number_of_passenger)

        finally:
            pass

    def click_on_more_option(self, action=None):

        '''
        :param action: "expand" / "collapse"
        '''

        try:
            if action == "expand":
                expand = self.driver.find_element(By.XPATH, Locators.more_option_validate)
                if expand.get_attribute('style').find(Locators.value_expand) < 0:
                    expand.click()
            elif action == "collapse":
                collapse = self.driver.find_element(By.XPATH, Locators.more_option_validate)
                if collapse.get_attribute('style').find(Locators.value_collapse) < 0:
                    collapse.click()
        finally:
            pass

    def enter_class_of_travel(self,class_of_travel="Economy"):
        '''
        class_of_travel = "economy"
        '''
        try:
            a_ele=Select(self.driver.find_element(By.XPATH,Locators.class_of_travel))
            a_ele.select_by_value(class_of_travel)
        finally:
            pass

    def enter_preferred_airline(self,preferred_airline=None):
        pass

    def click_on_search_flights(self):
        '''
        parameter
        '''
        try:
            self.driver.find_element(By.XPATH, Locators.search_flights_button).click()
            time.sleep(5)
        finally:
            pass

    def get_date_for_booking(self, days=None):

        date = datetime.now() + timedelta(days)
        return date.day, date.month, date.year







