import pytest
from assertpy import assert_that
from selenium import webdriver

from pages.login_page import LoginPage

"""scope=class -- browser launch """


@pytest.mark.usefixtures("browser_config")
class TestLoginUI1:
    def test_title(self):
        print(self.my_name)
        actual_title = self.driver.title
        assert_that('OrangeHRM').is_equal_to(actual_title)

    def test_placeholder(self):
        login_page = LoginPage(self.driver)
        assert_that('Username').is_equal_to(login_page.get_username_placeholder)
        assert_that('Password').is_equal_to(login_page.get_password_placeholder)


@pytest.mark.usefixtures("browser_config")
class TestLoginUI2:
    def test_title(self):
        actual_title = self.driver.title
        assert_that('OrangeHRM').is_equal_to(actual_title)
