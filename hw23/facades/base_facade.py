from hw23.pages.login_page import LoginPage
from hw23.pages.navigation_bar_page import NavigationBarPage
from hw23.pages.add_car_page import AddCar


class BaseFacade:

    def __init__(self):
        self.navigation_bar_page = NavigationBarPage()
        self.login_page = LoginPage()
        self.add_car_page = AddCar()