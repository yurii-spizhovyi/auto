from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from hw24.controls.button import Button
from hw24.controls.text_box import TextBox
from hw24.pages.base_page import BasePage


class AddCar(BasePage):
    def __init__(self):
        super().__init__()
        self.add_car_button = lambda: Button(self._driver.find_element(By.XPATH, "//button[text()='Add car']"))
        self.brand = lambda: Select(self._driver.find_element(By.ID, "addCarBrand"))
        self.mileage = lambda: TextBox(self._driver.find_element(By.ID, "addCarMileage"))
        self.add_button = lambda: Button(self._driver.find_element(By.XPATH, "//button[text()='Add']"))
