import allure

from hw25.constants.car_data import DEFAULT_MILEAGE
from hw25.facades.base_facade import BaseFacade


class AddCar(BaseFacade):
    def __init__(self):
        super().__init__()
    @allure.step("Test add car")
    def fill_fields(self, mileage=DEFAULT_MILEAGE):
        self.add_car_button()
        self.select_brand()
        self.put_mileage(mileage)
        self.click_add_button()
    @allure.step("Click Add Car button")
    def add_car_button(self):
        self.add_car_page.add_car_button().click()
    @allure.step("Select brand")
    def select_brand(self):
        self.add_car_page.brand().select_by_index(3)
    @allure.step("Put mileage")
    def put_mileage(self, mileage):
        self.add_car_page.mileage().send_keys(mileage)
    @allure.step("Click Add button")
    def click_add_button(self):
        self.add_car_page.add_button().click()
