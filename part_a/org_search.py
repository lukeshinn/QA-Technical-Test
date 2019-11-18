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

#     def test_navigate_to_login(self):
        # driver = self.driver
        # self.driver.get(config.url['home'])
        # main_page = page.MainPage(self.driver)
        # main_page.click_login_button()
        # login_page = page.LoginPage(self.driver)
        # assert login_page.check_for_login_form(), "No results found."

    def test_correct_login_credentials(self):
        driver = self.driver
        driver.get(config.url['login'])
        login_page = page.LoginPage(self.driver)
        login_page.fill_out_login_form(config.user['userName'], config.user['password'])
        response_page = page.ResponsePage(driver)
        assert response_page.is_successful(), 'Login was unsuccessful'

    def test_fake_login_credentials(self):
        driver = self.driver
        driver.get(config.url['login'])
        login_page = page.LoginPage(self.driver)
        fake = Faker()
        login_page.fill_out_login_form(fake.name(), 'password')
        response_page = page.ResponsePage(driver)
        assert response_page.is_successful(), 'Login was unsuccessful'


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='results'))
