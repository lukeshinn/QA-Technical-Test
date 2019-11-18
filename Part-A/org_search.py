import unittest
import HtmlTestRunner
import config
import page
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
        response_page = page.ResponsePage(self.driver)
        response_page.is_successful()
        assert response_page.is_successful(), 'Login was unsuccessful'


#     def test_login_correct_credentials(self):
        # driver = self.driver
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source

#     def test_search2_in_python_org(self):
        # driver = self.driver
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("gindlehelm")
        # elem.send_keys(Keys.RETURN)
        # # assert "No results found." not in driver.page_source

        # main_page = page.MainPage(self.driver)
        # assert main_page.is_title_matches(), "python.org title doesn't match."


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='results'))
