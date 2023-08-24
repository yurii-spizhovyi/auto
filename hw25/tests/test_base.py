import requests
import os

from selenium.webdriver.chrome import webdriver

from hw25.constants.url_constants import DEFAULT_URL
from hw25.driver.custom_driver import Driver
from hw25.facades.add_car_facade import AddCar
from hw25.facades.login_facade import LoginFacade


class TestBase:


    def setup_class(self):
        self.driver = Driver().driver
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.driver_path = os.path.join(self.script_dir, "C:/webdrivers/chromedriver.exe")

        self.driver.get(DEFAULT_URL)
        self.login_facade = LoginFacade()
        self.add_car_facade = AddCar()
        self.session = requests.session()