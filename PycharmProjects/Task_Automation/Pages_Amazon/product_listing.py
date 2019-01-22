from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from Locators_Amazon.Locators import Locators


class ProductListing:

    def _init_(self, driver):
        self.driver = driver

    def filter_by_format_type(self, format_type=None):
        '''
        :param format_type: "paperback" / "hardcover" / "kindle"
        :return:
        '''

        try:
            option = {"paperback":Locators.paper_back,
                      "hardcover":Locators.hard_cover,"kindle":Locators.kindle_books}

            if self.driver.find_element(By.XPATH,Locators.format_ele.format(option[format_type])).is_selected():
                print("Format type already selected")
            else:
                self.driver.find_element(By.XPATH, Locators.format_ele.format(option[format_type])).click()
        finally:
            pass

    def select_offers_link_in_product(self):

        try:
            ele = Locators.title_ele + Locators.select_choices
            ac = ActionChains(self.driver)
            ac.move_to_element(self.driver.find_element(By.XPATH, ele))
            ac.click(self.driver.find_element(By.XPATH, ele))
            ac.perform()
        finally:
            pass

    def switch_tabs_amazon(self, switch_to=None):

        try:
            tab_one, tab_two = self.driver.window_handles
            if switch_to == "one":
                switch_to = tab_one
            else:
                switch_to = tab_two
            self.driver.switch_to_window(switch_to)
        finally:
            pass

    def select_add_to_cart(self, rupees=None):

        try:
            ac = ActionChains(self.driver)
            ac.move_to_element(self.driver.find_element(By.XPATH, Locators.select_add_to_cart.format(rupees)))
            ac.click(self.driver.find_element(By.XPATH, Locators.select_add_to_cart.format(rupees)))
            ac.perform()
        finally:
            pass

    def select_from_list_of_book(self):

        try:
            a_eles = [i.text for i in self.driver.find_elements(By.XPATH, Locators.get_low_value)]
            a = []
            for i in a_eles:
                if "," in i:
                    i = i.replace(",", "")
                    a.append(float(i.strip()))
                else:
                    a.append(float(i.strip()))
            minimum_value = min(a)
            return minimum_value
        finally:
            pass


