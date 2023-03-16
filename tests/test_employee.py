from selenium.webdriver.common.by import By

from base.webdriver_listner import WebDriverWrapper


class TestAddEmployee(WebDriverWrapper):
    def test_add_valid_employee(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        """
 5. click on PIM
 6. Click on Add Employee
 7. Enter firstname
 8. Enter middlename
 9. Enter lastname
 10. Upload the employee image
    11. Add Employee header should be displayed
 12. Employee First Name should be displayed in the text box"""
