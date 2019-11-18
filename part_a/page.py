from element import BasePageElement
import config
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
            wait = WebDriverWait(self.driver, 4)
            login_form = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'login-container')))
            return login_form

        def fill_out_login_form(self, userId, userPass):

            input_email = self.driver.find_element_by_id('email')
            input_password = self.driver.find_element_by_id('password')
            input_submit = self.driver.find_element_by_id('logIn')
            input_email.send_keys(userId)
            input_password.send_keys(userPass)
            input_submit.click()
#             wait = WebDriverWait(self.driver, 10)
            # element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))


class element_has_css_class(object):

  def __init__(self, locator, css_class):
    self.locator = locator
    self.css_class = css_class

  def __call__(self, driver):
    element = driver.find_element(*self.locator)   # Finding the referenced element
    if self.css_class in element.get_attribute("class"):
        return element
    else:
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
                # element = wait.until(element_has_css_class((By.XPATH, '//div[@class="login-error"]'), "fade-in-expand"))
                user_nav_is_present = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="login-error"]')))
                return True
            except:
                return False
