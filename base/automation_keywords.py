from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AutomationKeywords:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 30)

    def type_by_locator(self, locator, text):
        self._wait.until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    def click_by_locator(self, locator):
        self._wait.until(expected_conditions.visibility_of_element_located(locator)).click()

    def get_text_by_locator(self, locator):
        return self._wait.until(expected_conditions.visibility_of_element_located(locator)).text

    def get_attribute_by_locator(self, locator, attribute):
        return self._wait.until(expected_conditions.visibility_of_element_located(locator)).get_attribute(attribute)

    def switch_tab_by_title(self, title):
        for window in self._driver.window_handles:
            self._driver.switch_to.window(window)
            if self._driver.title == title:
                break
