import pytest
from selenium.webdriver.common.by import By
from assertpy import assert_that
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.webdriver_listner import WebDriverWrapper
from pages.login_page import LoginPage
from pages.main_page import Mainpage
from utilities.data_source import DataSource


class TestAddEmployee(WebDriverWrapper):

    @pytest.mark.parametrize('username, password, firstname, middlename, lastname, expected_header,expected_firstname',
                             DataSource.test_add_valid_employee_data)
    def test_add_valid_employee(self, username, password, firstname, middlename, lastname, expected_header,
                                expected_firstname):

        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_on_login()

        main_page=Mainpage(self.driver)
        main_page.click_on_pim_menu()

        #PIMPage
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()

        #AddEmployeePage
        self.driver.find_element(By.NAME, "firstName").send_keys(firstname)
        self.driver.find_element(By.NAME, "middleName").send_keys(middlename)
        self.driver.find_element(By.NAME, "lastName").send_keys(lastname)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        #get data under PersonalPage
        actual_header = self.driver.find_element(By.XPATH, f"//h6[normalize-space()='{expected_header}']").text

        """ wait for firstname textbox contains firstname value """
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.text_to_be_present_in_element_attribute((By.NAME, "firstName"), 'value',
                                                                               expected_firstname))

        actual_first_name = self.driver.find_element(By.NAME, "firstName").get_attribute("value")

        assert_that(expected_header).is_equal_to(actual_header)
        assert_that(expected_firstname).is_equal_to(actual_first_name)
