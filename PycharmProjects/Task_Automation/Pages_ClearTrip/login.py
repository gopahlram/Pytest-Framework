# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from Locators.locators import Locators
# import sys
# sys.path.append("C:\\Users\\WittyParrot\\PycharmProjects")
# from Task_Automation.Locators import locators


class Login:

    '''
    Methods to Login into the clear trip application
    '''

    def _init_(self, driver):
        self.driver = driver

    def login(self, user_name=None, password=None):

        ### switching to Login Popup Iframe ###

        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, Locators.login_page_iframe))

        ### Entering user_name and password for login page ###

        self.driver.find_element(By.XPATH, Locators.user_name_txt_field).send_keys(user_name)
        self.driver.find_element(By.XPATH, Locators.passowrd_txt_field).send_keys(password)
        self.driver.find_element(By.XPATH, Locators.sign_in_button).click()
        self.driver.switch_to.default_content()








