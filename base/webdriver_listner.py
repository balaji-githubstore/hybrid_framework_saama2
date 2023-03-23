import pytest
from selenium import webdriver


class WebDriverWrapper:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        browser_name="ch"

        if browser_name=="edge":
            self.driver = webdriver.Edge()
        elif browser_name=="ff":
            self.driver=webdriver.Firefox()
        else:
            self.driver=webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        yield
        self.driver.quit()
