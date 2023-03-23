from selenium.webdriver.common.by import By

from base.automation_keywords import AutomationKeywords


class LoginPage(AutomationKeywords):

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver
        self.__username_locator = (By.NAME, "username")
        self.__password_locator = (By.NAME, "password")
        self.__login_locator = (By.XPATH, "//button[normalize-space()='Login']")
        self.__error_locator = (By.XPATH, "//p[contains(normalize-space(),'Invalid')]")
        self.__header_locator = (By.XPATH, "//h5")

    def enter_username(self, username):
        # self._driver.find_element(By.NAME, "username").send_keys(username)
        self.type_by_locator(self.__username_locator, username)

    def enter_password(self, password):
        # self.driver.find_element(By.NAME, "password").send_keys(password)
        self.type_by_locator((By.NAME, "password"), password)

    def click_on_login(self):
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.click_by_locator(self.__login_locator)

    @property
    def get_error_message(self):
        # return self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Invalid')]").text
        return self.get_text_by_locator(self.__error_locator)

    @property
    def get_header(self):
        # return self.driver.find_element(By.XPATH, "//h5").text
        return self.get_text_by_locator(self.__header_locator)

    @property
    def get_username_placeholder(self):
        # return self.driver.find_element(By.NAME, 'username').get_attribute('placeholder')
        return self.get_attribute_by_locator(self.__username_locator, "placeholder")

    @property
    def get_password_placeholder(self):
        # return self.driver.find_element(By.NAME, 'password').get_attribute('placeholder')
        return self.get_attribute_by_locator(self.__password_locator, "placeholder")
