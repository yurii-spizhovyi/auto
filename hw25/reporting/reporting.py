import allure
import allure_commons


@allure.feature('feature1')
@allure.suite("Suite 1")
class TestSomething:
    def test_success(self):
        assert True

    def test_failed(self):
        assert False
