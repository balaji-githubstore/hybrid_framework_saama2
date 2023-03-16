import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.webdriver_listner import WebDriverWrapper
from utilities.data_source import DataSource


class TestLogin(WebDriverWrapper):
    @pytest.mark.smoke
    def test_valid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        actual_header = self.driver.find_element(By.XPATH, "//h6[contains(normalize-space(),'Dash')]").text
        assert_that('Dashboard').is_equal_to(actual_header)

    @pytest.mark.parametrize('username,password,expected_error', DataSource.test_invalid_data)
    def test_invalid_login(self, username, password, expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        actual_error = self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Invalid')]").text
        assert_that(actual_error).contains(expected_error)


@pytest.mark.ui
class TestLoginUI(WebDriverWrapper):
    @pytest.mark.smoke
    def test_title(self):
        actual_title = self.driver.title
        assert_that('OrangeHRM').is_equal_to(actual_title)

    def test_placeholder(self):
        actual_username_placehodler = self.driver.find_element(By.NAME, 'username').get_attribute('placeholder')
        actual_password_placehodler = self.driver.find_element(By.NAME, 'password').get_attribute('placeholder')
        assert_that('Username').is_equal_to(actual_username_placehodler)
        assert_that('Password').is_equal_to(actual_password_placehodler)

    @pytest.mark.smoke
    def test_header(self):
        actual_header = self.driver.find_element(By.XPATH, "//h5").text
        assert_that('Login').is_equal_to(actual_header)
