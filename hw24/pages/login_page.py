from selenium.webdriver.common.by import By

from hw24.controls.text_box import TextBox
from hw24.controls.button import Button
from hw24.pages.base_page import BasePage
from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.email = lambda: TextBox(self._driver.find_element(By.ID, "signinEmail"))
        self.password = lambda: TextBox(self._driver.find_element(By.ID, "signinPassword"))
        self.login_button = lambda: Button(self._driver.find_element(By.XPATH, "//button[text()='Login']"))
