import pytest
from selenium import webdriver
import logging

LOGGER = logging.getLogger()


class WebDriverWrapper:
    driver = None

    @pytest.fixture(scope="function", autouse=True, params=["ch", "edge"])
    def browser_config(self, request):
        # print(request.param)
        browser_name = request.param

        if browser_name == "edge":
            self.driver = webdriver.Edge()
        elif browser_name == "ff":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        yield
        self.driver.quit()
