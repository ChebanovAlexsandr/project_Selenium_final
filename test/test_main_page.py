import time

import pytest
import allure
from base.base_test import BaseTest


class TestMainPage(BaseTest):
    @allure.title("Тест проверка главной страници и перехода на страницу товара")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_main_page(self):
        self.main_page.open()
        self.main_page.text_verification("Их покупают повторно")
        self.main_page.is_opened()
        self.main_page.clock_burger_menu()
        self.main_page.click_man("В корзину")
        time.sleep(5)
