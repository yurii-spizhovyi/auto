import requests
import json
import os


class TestUserCreateLoginDelete:

    def setup_class(self):
        self.session = requests.Session()  # Create a session to persist cookies
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the JSON file using os.path.join()
        json_file_path = os.path.join(script_dir, "test_data.json")

        with open(json_file_path) as config:
            self.json_data = json.load(config)

    def test_registration_user(self):
        result = self.session.post(url='https://qauto2.forstudy.space/api/auth/signup', json=self.json_data)
        assert result.json()["status"] == "ok"

    def test_login_user(self):
        login_json = {
            "email": "yuriis@autotest.com",
            "password": "Qwerty12345",
            "remember": False
        }
        result = self.session.post(url='https://qauto2.forstudy.space/api/auth/signin', json=login_json)
        assert result.json()["status"] == "ok"

    def test_profile_user(self):
        result = self.session.get(url='https://qauto2.forstudy.space/api/users/profile')
        assert result.json()["status"] == "ok"

    def test_delete_user(self):
        result = self.session.delete(url="https://qauto2.forstudy.space/api/users/")
        assert result.json()["status"] == "ok"
