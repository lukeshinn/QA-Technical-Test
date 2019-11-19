import helpers
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

    def click_login_button(self):
        element = self.driver.find_element_by_class_name('login')
        element.click()


class LoginPage(BasePage):

        userId = None
        userPass = None

        def check_for_login_form(self):
            wait = WebDriverWait(self.driver, 4)
            login_form = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'login-container')))
            return login_form

        def fill_out_login_form(self, userId, userPass):

            input_email = self.driver.find_element_by_id('email')
            input_password = self.driver.find_element_by_id('password')
            input_email.send_keys(userId)
            input_password.send_keys(userPass)

        def click_submit_button(self):
            input_submit = self.driver.find_element_by_id('logIn')
            input_submit.click()

        def press_enter_button(self):
            input_submit = self.driver.find_element_by_id('logIn')
            input_submit.send_keys(Keys.RETURN)

        def login_input_color_is_black(self):
            input_email_color = self.driver.find_element_by_id('logIn').value_of_css_property('color')
            input_color = str(input_email_color)
            try:
                input_email_color == "rgba(255, 255, 255, 1)"
                return True
            except:
                return False


class ResponsePage(BasePage):

        def check_for_user_nav(self):
            wait = WebDriverWait(self.driver, 4)
            try:
                nav_is_present= wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="hui-globalusermenu"]')))
                return True
            except:
                return False

        def check_for_user_nav(self):
            wait = WebDriverWait(self.driver, 4)
            try:
                user_nav_is_present = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="hui-globalusermenu"]')))
                return True
            except:
                return False

        def login_error_has_visible_class(self):
            wait = WebDriverWait(self.driver, 4)
            try:
                user_nav_is_present = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="login-error"]')))
                return True
            except:
                return False
