import os
import sys
sys.path.append(os.path.abspath('../'))
from selenium import webdriver
from Pages_ClearTrip.user import User
from Locators.user_data import UserData
import time
import unittest
import HtmlTestRunner


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        root_path = os.path.expanduser('~').replace("\\","/")
        chrome_path = root_path + '/PycharmProjects/Task_Automation/drivers/chromedriver.exe'
        cls.driver = webdriver.Chrome(executable_path=chrome_path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_one_flow(self):

        driver = self.driver
        driver.get("https://www.cleartrip.com")

        user = User(self.driver)
        user.click_on_login_button()
        time.sleep(6)

        user.login(user_name=UserData.user_name, password=UserData.password)
        time.sleep(10)
        user.select_trip_type(trip_type="round")
        user.enter_travel_details(From_=UserData.From_, To_=UserData.To_)
        day, month, year = user.get_date_for_booking(days=10)
        user.select_calender(for_="depart", day=day, month=month-1, year=year)
        time.sleep(2)
        day, month, year = user.get_date_for_booking(days=11)
        user.select_calender(for_="return_date", day=day, month=month-1, year=year)
        user.enter_passenger_details(passenger_type="adult", number_of_passenger="1")
        user.enter_passenger_details(passenger_type="child", number_of_passenger="1")
        user.click_on_search_flights()
        time.sleep(20)
        airline = ["air_asia", "air_india", "goair", "jet", "sj", "vt"]
        user.select_deselect_airline(airline=airline, action="uncheck")
        user.sort_list_of_flights(route="BLR_DEL", sort="asc", sort_for="price")
        time.sleep(2)
        user.sort_list_of_flights(route="DEL_BLR", sort="desc", sort_for="depart")
        time.sleep(2)
        user.select_flight(route="BLR_DEL")
        user.select_flight(route="DEL_BLR")
        time.sleep(1)
        user.click_on_book()
        time.sleep(20)
        user.click_on_terms_and_conditions()
        user.click_on_continue_booking(for_="itinerary")
        time.sleep(5)
        adult_details = {"number": 1, "title": "Mr", "f_name": "Rajesh", "l_name": "Venkatraman"}
        user.enter_traveller_details(details_for="adult", adult=[adult_details])
        child_details = {"number": 1, "title": "Mstr", "f_name": "Aaron", "l_name": "Rajesh", "DOB": "12-1-2010"}
        user.enter_traveller_details(details_for="child", child=[child_details], mobile_no="8903413339")
        time.sleep(1)
        user.click_on_continue_booking(for_="travel")
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    root_path = os.path.expanduser('~').replace("\\", "/")
    report_path = root_path + '/PycharmProjects/Task_Automation/reports'
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=report_path))



