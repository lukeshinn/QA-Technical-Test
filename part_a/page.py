from element import BasePageElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def click_login_button(self):
        element = self.driver.find_element_by_class_name('login')
        element.click()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Python" in self.driver.title

class LoginPage(BasePage):

        userId = None
        userPass = None

        def check_for_login_form(self):
            wait = WebDriverWait(self.driver, 5)
            login_form = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'login-container')))
            return login_form

        def fill_out_login_form(self, userId, userPass):

            input_email = self.driver.find_element_by_id('email')
            input_password = self.driver.find_element_by_id('password')
            input_submit = self.driver.find_element_by_id('logIn')
            input_email.send_keys(userId)
            input_password.send_keys(userPass)
            input_submit.submit()
            # print(self.driver.page_source)

class ResponsePage(BasePage):

        def is_successful(self):

           return "\"success\":true" in self.driver.page_source
