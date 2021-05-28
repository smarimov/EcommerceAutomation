from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    """methods for automation"""

    def do_click(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text_in_box(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(by_locator))
        return element.text
