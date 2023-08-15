from hw23.driver.custom_driver import Driver


class BasePage:

    def __init__(self):
        self._driver = Driver().driver
