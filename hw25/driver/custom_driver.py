import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Driver:
    def __init__(self):
        self.service = webdriver.chrome.service.Service(executable_path=r'C:/web_drivers/chromedriver.exe')
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        self.driver.implicitly_wait(5)
