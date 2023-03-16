import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By


class TestLoginUI:
    @pytest.fixture(scope="function",autouse=True)
    def browser_config(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        yield
        self.driver.quit()

    def test_title(self):
        actual_title = self.driver.title
        assert_that('OrangeHRM').is_equal_to(actual_title)

    def test_placeholder(self):
        actual_username_placehodler = self.driver.find_element(By.NAME, 'username').get_attribute('placeholder')
        actual_password_placehodler = self.driver.find_element(By.NAME, 'password').get_attribute('placeholder')
        assert_that('Username').is_equal_to(actual_username_placehodler)
        assert_that('Password').is_equal_to(actual_password_placehodler)

    def test_header(self):
        actual_header=self.driver.find_element(By.XPATH,"//h5").text
        assert_that('Login').is_equal_to(actual_header)