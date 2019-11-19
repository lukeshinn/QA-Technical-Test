import unittest
import HtmlTestRunner
import config
import page
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_navigate_to_login(self):
        """test if user can navigate to login page by clicking the login button"""
        driver = self.driver
        # load homepage and initiate main_page
        self.driver.get(config.url['home'])
        main_page = page.MainPage(self.driver)
        # click login button on hudl.com
        main_page.click_login_button()
        # initiate login page to see if login form is present
        login_page = page.LoginPage(self.driver)
        # positive check for presence of login form after you click login
        assert login_page.check_for_login_form(), "No results found."

    def test_correct_login_credentials(self):
        """test if user can login with correct credentials"""
        driver = self.driver
        # load hudl.com/login
        driver.get(config.url['login'])
        login_page = page.LoginPage(self.driver)
        login_page.fill_out_login_form(config.user['userName'], config.user['password'])
        login_page.click_submit_button()
        # get response of login form submission
        response_page = page.ResponsePage(driver)
        # positive check to see if the user navigation is present
        assert response_page.check_for_user_nav(), 'User navigation is not present'

    def test_fake_login_credentials(self):
        """test to see if the login error element has the class '.login-error' which makes the div visible"""
        driver = self.driver
        # variable to create fake data, this will be different data
        # every tme you run the driver
        fake = Faker()
        driver.get(config.url['login'])
        login_page = page.LoginPage(self.driver)
        # fill out form with fake name and a weak password
        login_page.fill_out_login_form(fake.name(), 'password')
        login_page.click_submit_button()
        response_page = page.ResponsePage(driver)
        # negative check to make sure the user cannot login with incorrect credentials
        assert response_page.login_error_has_visible_class(), 'Login was unsuccessful'

    def test_blank_password_entry(self):
        """test to see if login error element has error class when a form is entered with no password"""
        driver = self.driver
        fake = Faker()
        driver.get(config.url['login'])
        login_page = page.LoginPage(self.driver)
        response_page = page.ResponsePage(driver)
        login_page.fill_out_login_form(fake.name(), '')
        login_page.click_submit_button()
        assert response_page.login_error_has_visible_class(), 'Error message never received visible class'

    def test_correct_login_with_enter_button(self):
        """test if user can login with correct credentials"""
        driver = self.driver
        # load hudl.com/login
        driver.get(config.url['login'])
        login_page = page.LoginPage(self.driver)
        login_page.fill_out_login_form(config.user['userName'], config.user['password'])
        login_page.press_enter_button()
        # get response of login form submission
        response_page = page.ResponsePage(driver)
        # positive check to see if the user navigation is present
        assert response_page.check_for_user_nav(), 'User navigation is not present'

    def test_login_email_input_is_color_black(self):
        """test if the css color value of the email input is black"""
        driver = self.driver
        # load hudl.com/login
        driver.get(config.url['login'])
        login_page = page.LoginPage(self.driver)
        assert login_page.login_input_color_is_black(), "Login form color is not black"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='results'))
