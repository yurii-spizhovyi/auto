from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import json
import os
from selenium.webdriver.support.ui import Select


class TestUserCreateThenLoginThenCarAddAndAfterAllDelete:

    def setup_class(self):
        self.session = requests.Session()  # Create a session to persist cookies
        # Get the directory of the current script
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.driver_path = os.path.join(self.script_dir, "C:/webdrivers/chromedriver.exe")
        # Construct the path to the JSON file using os.path.join()
        json_file_path = os.path.join(self.script_dir, "test_data.json")
        with open(json_file_path) as config:
            self.json_data = json.load(config)
        self.email = self.json_data['email']
        self.password = self.json_data['password']
        self.session = requests.Session()  # Create a session to persist cookies

    def test_registration_user(self):
        """
        Function for user creation
        :return:
        """
        result = self.session.post(url='https://qauto2.forstudy.space/api/auth/signup', json=self.json_data)
        assert result.json()["status"] == "ok"

    def test_login_add_car_and_then_delete_all(self):
        """
        Function for login, add a car, get car id, then delete car and user
        :return:
        """
        self.driver = webdriver.Chrome(self.driver_path)
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        self.driver.implicitly_wait(2)
        # user login
        sign_in_button = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        sign_in_button.click()
        email_field = self.driver.find_element(By.ID, "signinEmail")
        password_field = self.driver.find_element(By.ID, "signinPassword")
        email_field.send_keys(self.email)
        password_field.send_keys(self.password)
        self.driver.find_element(By.XPATH, "//button[text()='Login']").click()
        # add car
        add_car_button = self.driver.find_element(By.XPATH, "//button[text()='Add car']")
        add_car_button.click()
        # select brand
        drop_down_select_brand = self.driver.find_element(By.ID, "addCarBrand")
        select_brand = Select(drop_down_select_brand)
        select_brand.select_by_index(3)
        # put mileage
        mileage = self.driver.find_element(By.ID, "addCarMileage")
        mileage.send_keys("100000")
        # add car
        add_button = self.driver.find_element(By.XPATH, "//button[text()='Add']")
        add_button.click()
        self.driver.close()
        # get car id
        result_car_id = self.session.get(url='https://qauto2.forstudy.space/api/cars')
        response = result_car_id.json()["data"]
        for item in response:
            car_id = item['id']
        # delete car by car id
        delete_car_url = f"https://qauto2.forstudy.space/api/cars/{car_id}"
        delete_car = self.session.delete(url=delete_car_url)
        assert delete_car.json()["status"] == "ok"
        # delete current user
        delete_user = self.session.delete(url="https://qauto2.forstudy.space/api/users/")
        assert delete_user.json()["status"] == "ok"
