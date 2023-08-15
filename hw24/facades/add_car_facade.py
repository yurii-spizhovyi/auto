from hw24.constants.car_data import DEFAULT_MILEAGE
from hw24.facades.base_facade import BaseFacade


class AddCar(BaseFacade):
    def __init__(self):
        super().__init__()

    def fill_fields(self, mileage=DEFAULT_MILEAGE):
        self.add_car_button()
        self.select_brand()
        self.put_mileage(mileage)
        self.click_add_button()

    def add_car_button(self):
        self.add_car_page.add_car_button().click()

    def select_brand(self):
        self.add_car_page.brand().select_by_index(3)

    def put_mileage(self, mileage):
        self.add_car_page.mileage().send_keys(mileage)

    def click_add_button(self):
        self.add_car_page.add_button().click()
