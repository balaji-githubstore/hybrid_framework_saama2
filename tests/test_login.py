import assertpy
import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.webdriver_listner import WebDriverWrapper
from base import webdriver_listner
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utilities.data_source import DataSource


class TestLogin(WebDriverWrapper):
    @pytest.mark.smoke
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_on_login()

        dashboard_page = DashboardPage(self.driver)
        actual_header = dashboard_page.get_header

        assert_that('Dashboard').is_equal_to(actual_header)

    @pytest.mark.invalid
    @pytest.mark.parametrize('username,password,expected_error', DataSource.test_invalid_data_csv)
    def test_invalid_login(self, username, password, expected_error):
        try:
            login_page = LoginPage(self.driver)
            login_page.enter_username(username)
            webdriver_listner.LOGGER.info("Entered Username " + username)
            login_page.enter_password(password)
            webdriver_listner.LOGGER.info("Entered Password " + password)
            login_page.click_on_login()
            webdriver_listner.LOGGER.info("Clicked on login")

            actual_error = login_page.get_error_message
            webdriver_listner.LOGGER.info("Actual Error Message" + actual_error)
            assert_that(actual_error).contains(expected_error)
        except BaseException as error:
            webdriver_listner.LOGGER.error("Failure" + error)
            assertpy.fail("test_invalid_login")


@pytest.mark.ui
class TestLoginUI(WebDriverWrapper):
    @pytest.mark.smoke
    def test_title(self):
        actual_title = self.driver.title
        assert_that('OrangeHRM').is_equal_to(actual_title)

    def test_placeholder(self):
        login_page = LoginPage(self.driver)
        assert_that('Username').is_equal_to(login_page.get_username_placeholder)
        assert_that('Password').is_equal_to(login_page.get_password_placeholder)

    @pytest.mark.smoke
    def test_header(self):
        login_page = LoginPage(self.driver)
        assert_that('Login').is_equal_to(login_page.get_header)
