import os
import json
import allure
from allure_commons.types import AttachmentType

from hw25.api.delete_car import DeleteCar
from hw25.constants.api_path_constants import POST_SIGN_IN_USER, DELETE_USER, POST_SIGN_UP_USER
from hw25.constants.url_constants import DEFAULT_API_URL
from hw25.constants.user_credentials import USER_EMAIL, USER_PASSWORD
from hw25.tests.test_base import TestBase


@allure.suite("AddingCarTest")
class TestAddCar(TestBase):

    def setup_class(self):
        super().setup_class(self)
        json_file_path = os.path.join(self.script_dir, "../test_data.json")
        with open(json_file_path) as config:
            self.json_data = json.load(config)

        self.user_to_delete = {
            "email": USER_EMAIL,
            "password": USER_PASSWORD,
            "remember": False
        }

    def teardown_class(self):
        self.session.post(url=f"{DEFAULT_API_URL}{POST_SIGN_IN_USER}", json=self.user_to_delete)
        self.session.delete(f"{DEFAULT_API_URL}{DELETE_USER}")

    @allure.step("Test user registration")
    def test_registration_user(self):
        result = self.session.post(url=f'{DEFAULT_API_URL}{POST_SIGN_UP_USER}', json=self.json_data)
        assert result.json()["status"] == "ok"
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.step("Test user login")
    def user_login(self):
        self.login_facade.login_user()

    @allure.step("Test add car")
    def test_add_car(self):
        self.user_login()
        self.add_car_facade.fill_fields()
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        self.driver.close()

    @allure.step("Test delete car")
    def test_delete_car_by_id(self):
        self.delete_car = DeleteCar()
