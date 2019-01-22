from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from Locators_Amazon.Locators import Locators
import time


class Login:

    def _init_(self, driver):

        self.driver = driver

    def login_into_amazon(self, user_name=None, password=None):

        '''
        :param user_name: "amazon account user name"
        :param password: "amazon account passwors"
        :return:
        '''

        try:
            self.driver.find_element(By.XPATH, Locators.email_field).send_keys(user_name)
            self.driver.find_element(By.XPATH,Locators.login_continue_button).send_keys(Keys.ENTER)
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, Locators.login_button)),
                                                  "Page takes time to move further after email entered")
            self.driver.find_element(By.XPATH, Locators.password_field).send_keys(password)
            self.driver.find_element(By.XPATH, Locators.login_button).send_keys(Keys.ENTER)
            time.sleep(5)
        finally:
            pass