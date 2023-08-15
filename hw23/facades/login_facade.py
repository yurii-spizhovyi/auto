from hw23.constants.user_credentials import USER_EMAIL, USER_PASSWORD
from hw23.facades.base_facade import BaseFacade


class LoginFacade(BaseFacade):
    def __init__(self):
        super().__init__()

    def fill_all_fields_on_login_form_with_correct_data(self, email=USER_EMAIL, password=USER_PASSWORD, is_click=True):
        self.fill_email_field_on_login_form(email)
        self.fill_password_on_login_form(password)

        if is_click:
            self.click_login_button()

    def login_user(self, email=USER_EMAIL, password=USER_PASSWORD):
        self.click_login_button_on_login_form()

        self.fill_all_fields_on_login_form_with_correct_data(email, password)

    def fill_email_field_on_login_form(self, email):
        self.login_page.email().send_keys(email)

    def fill_password_on_login_form(self, password):
        self.login_page.password().send_keys(password)

    def click_login_button(self):
        self.login_page.login_button().click()

    def click_login_button_on_login_form(self):
        self.navigation_bar_page.sign_in_button().click()
