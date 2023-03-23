from selenium.webdriver.common.by import By
from base.automation_keywords import AutomationKeywords


class Mainpage(AutomationKeywords):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver
        self.__pim_menu_locator = (By.XPATH, "//span[normalize-space()='PIM']")

    def click_on_pim_menu(self):
        self.click_by_locator(self.__pim_menu_locator)
