from hw24.constants.api_path_constants import DELETE_CARS
from hw24.constants.url_constants import DEFAULT_API_URL

from hw24.tests.test_base import TestBase


class DeleteCar(TestBase):
    def __init__(self):
        super().__init__()

    def test_delete_car_by_id(self):
        result_car_id = self.session.get(url=f'{DEFAULT_API_URL}{DELETE_CARS}')
        response = result_car_id.json()["data"]
        car_id = 0
        for item in response:
            car_id = item['id']
        delete_car_url = f"{DEFAULT_API_URL}{DELETE_CARS}/{car_id}"
        delete_car = self.session.delete(url=delete_car_url)
        assert delete_car.json()["status"] == "ok"
