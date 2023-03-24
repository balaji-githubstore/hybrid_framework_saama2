from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__header_locator = (By.XPATH, "//h6[contains(normalize-space(),'Dash')]")

    @property
    def get_header(self):
        # return self.driver.find_element(By.XPATH, "//h6[contains(normalize-space(),'Dash')]").text
        return self.get_text_by_locator(self.__header_locator)
