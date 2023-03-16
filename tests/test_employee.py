from selenium.webdriver.common.by import By
from assertpy import assert_that
from base.webdriver_listner import WebDriverWrapper


class TestAddEmployee(WebDriverWrapper):
    def test_add_valid_employee(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH,"//span[normalize-space()='PIM']").click()
        self.driver.find_element(By.LINK_TEXT,"Add Employee").click()
        self.driver.find_element(By.NAME, "firstName").send_keys("John")
        self.driver.find_element(By.NAME, "middleName").send_keys("W")
        self.driver.find_element(By.NAME, "lastName").send_keys("Wick")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        actual_header=self.driver.find_element(By.XPATH,"//h6[normalize-space()='John Wick']").text
        actual_first_name=self.driver.find_element(By.NAME, "firstName").get_attribute("value")
        assert_that('John Wick').is_equal_to(actual_header)
        assert_that('John').is_equal_to(actual_first_name)
