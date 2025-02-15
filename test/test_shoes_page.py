import time

import pytest
import allure
from base.base_test import BaseTest


class TestShoesPage(BaseTest):
    """Создали наш тестовый класс направленные на какуето фичу"""

    @allure.title("Тест проверка главной страници")
    @allure.severity("Normal")
    @pytest.mark.regression
    def test_main_page(self):
        self.shoes_page.open()
        self.shoes_page.text_verification("Обувь")
        self.shoes_page.is_opened()

    @allure.title("Тест проверки заполнения фильтров")
    @allure.severity("Normal")
    @pytest.mark.feature
    @pytest.mark.parametrize("arg1,arg2", [
        (0, 1),
        (1, 1000000000000000000000),
        (0, 6000),
        (101, 2005)
    ])
    def test_filter(self, arg1, arg2):
        self.shoes_page.open()
        self.shoes_page.is_opened()
        self.shoes_page.filter_test(arg1, arg2)

    @allure.title("Нигативный тест проверки заполнения фильтров")
    @allure.severity("Normal")
    @pytest.mark.feature
    @pytest.mark.parametrize("arg1,arg2,fill_both", [
        (100, -1100, True),
        (-100, 1100, False)
    ])
    def test_filter_negative(self, arg1, arg2, fill_both):
        self.shoes_page.open()
        self.shoes_page.is_opened()
        self.shoes_page.filter_test_negative(arg1, arg2, fill_both)


