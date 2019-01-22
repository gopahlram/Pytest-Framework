'''

Methods for Flight bokking page
'''

from selenium.webdriver.common.by import By
from Locators.locators import Locators
from selenium.webdriver.support.ui import Select


class FlightBooking:

    def __init__(self, driver):
        self.driver = driver

    def click_on_terms_and_conditions(self):

        try:
            self.driver.find_element(By.XPATH, Locators.click_agree).click()
        finally:
            pass

    def click_on_continue_booking(self,for_=None):
        try:
            if for_=="itinerary":
                self.driver.find_element(By.XPATH, Locators.continue_booking_btn).click()
            else:
                self.driver.find_element(By.XPATH, Locators.contine_travel).click()
        finally:
            pass

    def enter_email_address(self, email=None):

        try:
            self.driver.find_element(By.XPATH, Locators.enter_email_address).send_keys(email)
        finally:
            pass

    def enter_traveller_details(self, details_for = None, adult=[], child=[], mobile_no=None):

        '''
        :param adult:  {number : 1 ,"title":"a","f_name":"a","l_name":"b"}
        :param child:  {number = 1 ,"title":"a","f_name":"a","l_name":"b","DOB" "day-month-year"}
        :param mobile_no: "mobile_number"
        '''

        try:
            if details_for == "adult":
                for i in adult:
                    parent_loc = Locators.parent_locator.format(i["number"])
                    a_ele = Select(self.driver.find_element(By.XPATH, parent_loc + Locators.to_enter_title))
                    a_ele.select_by_value("Mr")

                    self.driver.find_element(By.XPATH, parent_loc + Locators.to_enter_first_name).clear()
                    self.driver.find_element(By.XPATH, parent_loc + Locators.to_enter_first_name).send_keys(i["f_name"])

                    self.driver.find_element(By.XPATH, parent_loc + Locators.to_enter_last_name).clear()
                    self.driver.find_element(By.XPATH, parent_loc + Locators.to_enter_last_name).send_keys(i["l_name"])

            elif details_for == "child":

                for i in child:
                    dob = i["DOB"].split("-")

                    day, month, year = dob
                    print(day, month, year)
                    parent_loc = Locators.p_l_one.format(i["number"])


                    #### To enter child details ####

                    a_ele = Select(self.driver.find_element(By.XPATH, parent_loc + Locators.to_enter_title))
                    a_ele.select_by_value("Mstr")

                    self.driver.find_element(By.XPATH, parent_loc + Locators.to_enter_first_name).clear()
                    self.driver.find_element(By.XPATH, parent_loc + Locators.to_enter_first_name).send_keys(i["f_name"])

                    self.driver.find_element(By.XPATH, parent_loc + Locators.to_enter_last_name).clear()
                    self.driver.find_element(By.XPATH, parent_loc + Locators.to_enter_last_name).send_keys(i["l_name"])

                    #### To select DOB ###

                    b_ele = Select(self.driver.find_element(By.XPATH, Locators.to_select_dob.format("day")))
                    b_ele.select_by_value(day)
                    b_ele = Select(self.driver.find_element(By.XPATH, Locators.to_select_dob.format("month")))
                    b_ele.select_by_value(month)
                    b_ele = Select(self.driver.find_element(By.XPATH, Locators.to_select_dob.format("year")))
                    b_ele.select_by_value(year)

                    #### Enter Mobile number ###

                    self.driver.find_element(By.XPATH, Locators.to_enter_mobile_num).clear()
                    self.driver.find_element(By.XPATH, Locators.to_enter_mobile_num).send_keys(mobile_no)

            else:
                pass


        finally:
            pass
