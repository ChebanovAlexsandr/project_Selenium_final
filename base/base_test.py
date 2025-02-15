import pytest
from pages.main_page import MainPage
from pages.shoes_page import ShoesPage
from pages.cart_page import CartPage

"""Создал класс что бы не инециализировать классы в тестах"""


class BaseTest:
    main_page: MainPage
    shoes_page: ShoesPage
    cart_page: CartPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver

        request.cls.main_page = MainPage(driver)
        request.cls.shoes_page = ShoesPage(driver)
        request.cls.cart_page = CartPage(driver)
