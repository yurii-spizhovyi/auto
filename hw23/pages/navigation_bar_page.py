from selenium.webdriver.common.by import By

from hw23.controls.button import Button
from hw23.pages.base_page import BasePage


class NavigationBarPage(BasePage):
    def __init__(self):
        super().__init__()
        self.sign_in_button = lambda: Button(self._driver.find_element(By.XPATH, "//button[text()='Sign In']"))
