from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import TestData


class TestLogin(BaseTest):
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

    def test_do_go_back_home_page(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.do_go_back_home_page()
        assert flag



