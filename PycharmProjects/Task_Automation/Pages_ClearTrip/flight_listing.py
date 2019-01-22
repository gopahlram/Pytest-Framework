'''
Methods for Flight Listing page
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators.locators import Locators
from selenium.webdriver import ActionChains
import time


class FlightListing:

    def _init_(self, driver):

        self.driver = driver

    def select_stops_from_filter(self, action=None, no_of_stops=None):

        try:

            var = Locators.to_click_filters.format(Locators.st_variable, no_of_stops)
            if action == "select":
                if self.driver.find_element(By.XPATH, var).is_selected():
                    print("User already selected the option '{0}'".format(no_of_stops))
                else:
                    acs = ActionChains(self.driver)
                    acs.move_to_element(self.driver.find_element(By.XPATH, var))
                    acs.click(self.driver.find_element(By.XPATH, var))
                    acs.perform()

            elif action == "deselect":

                if self.driver.find_element(By.XPATH, var).is_selected():
                    acd = ActionChains(self.driver)
                    acd.move_to_element(self.driver.find_element(By.XPATH, var))
                    acd.click(self.driver.find_element(By.XPATH, var))
                    acd.perform()
                else:
                    print("User already deselected the option '{0}'".format(no_of_stops))
        finally:
            pass

    def expand_filters(self, action=None, filter_type=None):
        """
        action = "expand" / "collapse"
        filter_type = "stops" / "dep" / "arrival" / "airlines"
        """

        try:
            option = {"stops":Locators.st_variable,"dep":Locators.d_t_variable,"arrival":Locators.a_t_variable,
                      "airlines":Locators.airline_variable}

            expand_val = self.driver.find_element(By.XPATH, Locators.to_validate_arrow.format(option[filter_type]))
            ex_coll_icon = self.driver.find_element(By.XPATH, Locators.click_expand_icon.format(option[filter_type]))
            if action == "expand":
                if expand_val.get_attribute('class').find(Locators.stops_expand) < 0:
                    ex_coll_icon.click()
                    time.sleep(2)
                else:
                    print("User already expanded the filter '{0}' tab".format(filter_type))

            elif action == "collapse":
                if expand_val.get_attribute('class').find(Locators.stops_collapse) < 0:
                    ex_coll_icon.click()
                    time.sleep(2)
                else:
                    print("User already collapsed the filter '{0}' tab".format(filter_type))
            else:
                pass
        finally:
            pass

    def select_departure_time_from_filter(self, action=None, dep_time=None):

        try:

            option = {"early_mon": "Early Morning", "mor": "Morning", "mid-day": "Mid-Day", "eve": "Evening",
                      "night": "Night"}

            if dep_time in option:
                dep_time = option[dep_time]
            var = Locators.to_click_filters_01.format(Locators.d_t_variable, dep_time)

            if action == "select":
                if self.driver.find_element(By.XPATH, var).is_selected():
                    print("User already selected the option '{0}'".format(dep_time))
                else:
                    self.driver.find_element(By.XPATH, var).click()
            elif action == "deselect":
                if not self.driver.find_element(By.XPATH, var).is_selected():
                    self.driver.find_element(By.XPATH, var).click()
                else:
                    print("User already selected the option '{0}'".format(dep_time))

        finally:
            pass

    def select_return_time_from_filter(self, action=None, return_time=None):

        try:
            option = {"early_mon": "Early Morning", "mor": "Morning", "mid-day": "Mid-Day", "eve": "Evening",
                      "night": "Night"}

            if return_time in option:
                return_time = option[return_time]

            var = Locators.to_click_filters.format(Locators.a_t_variable, return_time)

            if action == "select":
                if self.driver.find_element(By.XPATH, var).is_selected():
                    print("User already selected the option '{0}'".format(return_time))
                else:
                    self.driver.find_element(By.XPATH, var).click()

            elif action == "deselect":
                if not self.driver.find_element(By.XPATH, var).is_selected():
                    self.driver.find_element(By.XPATH, var).click()
                else:
                    print("User already deselected the option '{0}'".format(return_time))

        finally:
            pass

    def sort_list_of_flights(self, route=None, sort=None, sort_for=None):

        '''
        route = "BLR_DESC"
        sort = "asc" / "desc"
        sort_for = "airline" / "depart" / "duration" / "price"
        '''

        try:
            options = {"airline": "Airline", "depart": "dep", "duration": "dur", "price": "price"}
            sort_ele = self.driver.find_element(By.XPATH, Locators.select_asc_desc.format(route, options[sort_for]))
            sort_ele.click()

            if sort == "asc":
                if sort_ele.get_attribute('class').find(Locators.asc_variable) < 0:
                    sort_ele.click()
            elif sort == "desc":
                if sort_ele.get_attribute('class').find(Locators.desc_variable) < 0:
                    sort_ele.click()
        finally:
            pass

    def click_on_book(self):

        try:
            self.driver.find_element(By.XPATH, Locators.click_book).click()
        finally:
            pass

    def select_only_in_airlines(self, airline=None):

        try:
            ac = ActionChains(self.driver)
            ac.move_to_element(self.driver.find_element(By.XPATH, Locators.hover_select.format("IndiGo")))
            # ac.click(self.driver.find_element(By.XPATH, Locators.only_select.format(airline)))
            ac.perform()
        finally:
            pass

    def select_deselect_airline(self, airline=[], action=None):

        try:
            option = {"air_asia":"Air Asia","air_india":"Air India","goair":"GoAir",
                      "indigo":"IndiGo","jet":"Jet Airways","sj":"SpiceJet",
                      "vt":"Vistara"}

            for i in airline:

                if i in option:
                    i = option[i]

                if action == "check":
                    if self.driver.find_element(By.XPATH, Locators.sel_airline.format(i)).is_selected():
                        print("Airline checked already")
                    else:
                        self.driver.find_element(By.XPATH, Locators.sel_airline.format(i)).click()

                else:
                    if self.driver.find_element(By.XPATH, Locators.sel_airline.format(i)).is_selected():
                        self.driver.find_element(By.XPATH, Locators.sel_airline.format(i)).click()

                    else:
                        print("Airline unchecked already")
        finally:
            pass

    def select_flight(self, route=None):

        self.driver.find_element(By.XPATH, Locators.select_flight.format(route)).click()
