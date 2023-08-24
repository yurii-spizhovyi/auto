from selenium.webdriver.common.by import By

from hw25.controls.text_box import TextBox
from hw25.controls.button import Button
from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.email = lambda: TextBox(self._driver.find_element(By.ID, "signinEmail"))
        self.password = lambda: TextBox(self._driver.find_element(By.ID, "signinPassword"))
        self.login_button = lambda: Button(self._driver.find_element(By.XPATH, "//button[text()='Login']"))
