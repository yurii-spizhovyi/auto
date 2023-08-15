import os

from selenium import webdriver


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
        #self.driver = webdriver.Chrome()

        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.driver_path = os.path.join(self.script_dir, "C:/webdrivers/chromedriver.exe")
        chrome_service = webdriver.chrome.service.Service(self.driver_path)
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.implicitly_wait(5)