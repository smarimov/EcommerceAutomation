from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    """By locators"""
    SIGN_IN_BUTTON = (By.LINK_TEXT, 'Sign in')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    SUBMIT_BUTTON = (By.NAME, 'SubmitLogin')
    BACK_HOME_PAGE = (By.XPATH, '//img[@class="logo img-responsive"]')

    """Constructor of the LoginPage class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions for Login Page"""

    """this is used to sign in the website"""

    def do_login(self, username, password):
        self.do_click(self.SIGN_IN_BUTTON)
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.SUBMIT_BUTTON)

    def do_go_back_home_page(self):
        self.do_click(self.BACK_HOME_PAGE)


