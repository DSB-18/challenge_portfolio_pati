import os
import time
import unittest
from selenium import webdriver

from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_into_system(self):
        user_login = LoginPage(self.driver)
        user_login.page_title()
        #base_page = BasePage(self)
        #base_page.assert_element_text()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.page_title()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()