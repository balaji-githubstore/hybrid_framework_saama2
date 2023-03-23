from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, "username").send_keys(username)

    def enter_password(self, username):
        self.driver.find_element(By.NAME, "password").send_keys(username)

    def click_on_login(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    @property
    def get_error_message(self):
        return self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Invalid')]").text

    @property
    def get_header(self):
        return self.driver.find_element(By.XPATH, "//h5").text

    @property
    def get_username_placeholder(self):
        return self.driver.find_element(By.NAME, 'username').get_attribute('placeholder')

    @property
    def get_password_placeholder(self):
        return self.driver.find_element(By.NAME, 'password').get_attribute('placeholder')
