from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import requests
import json


class TestUserCreateThenLoginThenCarAddAndAfterAllDelete:

    def setup_class(self):
        self.session = requests.Session()
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.driver_path = os.path.join(self.script_dir, "C:/webdrivers/chromedriver.exe")
        json_file_path = os.path.join(self.script_dir, "test_data.json")
        with open(json_file_path) as config:
            self.json_data = json.load(config)
        self.email = self.json_data['email']
        self.password = self.json_data['password']

    def teardown_class(self):
        user_to_delete = {
            "email": self.email,
            "password": self.password,
            "remember": False
        }

        self.session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=user_to_delete)
        self.session.delete("https://qauto2.forstudy.space/api/users")

    def test_registration_user(self):
        result = self.session.post(url='https://qauto2.forstudy.space/api/auth/signup', json=self.json_data)
        assert result.json()["status"] == "ok"

    def user_login(self):
        chrome_service = webdriver.chrome.service.Service(self.driver_path)
        self.driver = webdriver.Chrome(service=chrome_service)

        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        self.driver.implicitly_wait(2)

        sign_in_button = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        sign_in_button.click()

        email_field = self.driver.find_element(By.ID, "signinEmail")
        password_field = self.driver.find_element(By.ID, "signinPassword")
        email_field.send_keys(self.email)
        password_field.send_keys(self.password)

        self.driver.find_element(By.XPATH, "//button[text()='Login']").click()

    def test_add_car(self):
        self.user_login()

        add_car_button = self.driver.find_element(By.XPATH, "//button[text()='Add car']")
        add_car_button.click()

        drop_down_select_brand = self.driver.find_element(By.ID, "addCarBrand")
        select_brand = Select(drop_down_select_brand)
        select_brand.select_by_index(3)

        mileage = self.driver.find_element(By.ID, "addCarMileage")
        mileage.send_keys("100000")

        # drop_down_select_model = self.driver.find_element(By.ID, "addCarModel")
        # select_model = Select(drop_down_select_model)
        # select_model.select_by_index(1)

        add_button = self.driver.find_element(By.XPATH, "//button[text()='Add']")
        add_button.click()
        self.driver.close()

    def test_delete_car_by_id(self):
        result_car_id = self.session.get(url='https://qauto2.forstudy.space/api/cars')
        response = result_car_id.json()["data"]
        car_id = 0
        for item in response:
            car_id = item['id']
        delete_car_url = f"https://qauto2.forstudy.space/api/cars/{car_id}"
        delete_car = self.session.delete(url=delete_car_url)
        assert delete_car.json()["status"] == "ok"
