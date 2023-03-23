from selenium.webdriver.common.by import By


class Mainpage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_pim_menu(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()