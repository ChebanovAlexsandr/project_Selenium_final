import time

import pytest
import allure
from base.base_test import BaseTest


class TestCartPage(BaseTest):
    @allure.title("Тест добовления товара")
    @pytest.mark.smoke
    def test_cart_page(self):
        self.cart_page.open()
        self.cart_page.check_product()

    @pytest.mark.feature
    @allure.title("Сравнение товаров в корзине")
    def test_car(self):
        self.cart_page.open()
        self.cart_page.check_cart()

    @pytest.mark.regression
    @allure.title("Офорление заказа")
    def test_order(self):
        self.cart_page.open()
        self.cart_page.registration_order()
