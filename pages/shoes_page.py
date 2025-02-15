import time

import allure
from selenium.webdriver.common.by import By

from base.base_page import BasePage  # наследумся от нашего родительского класса для доступности наших методов
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ShoesPage(BasePage):
    PAGE_URL = Links.SHOES

    TEXT_SHOES = (By.CSS_SELECTOR, ".header___brtVq")
    FILTER_MENU_SORTED = (By.CSS_SELECTOR,
                          "body > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(7) > main:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1) > div:nth-child(1) > span:nth-child(2)")
    FILTER_PO_RETING = (By.CSS_SELECTOR,
                        "body > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(7) > main:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(5)")
    PRICE = (By.CSS_SELECTOR, "div[aria-label='Фильтрация списка товаров'] div:nth-child(2) button:nth-child(1)")
    PRECE_INPUT_1 = (By.CSS_SELECTOR, "input[placeholder='10,00 ₽']")
    PRECE_INPUT_2 = (By.CSS_SELECTOR, "input[placeholder='10 000,00 ₽']")
    CHILDREN_SHOES = (By.CSS_SELECTOR, "(//*[@class = 'name___DUa3t'])[7]")

    @allure.step("Text verification")
    def text_verification(self, text):
        self.driver.implicitly_wait(5)
        t = self.find(self.TEXT_SHOES)
        assert text == t.text, "Ошибка текст не верный"

    @allure.step("Заполнение фильтра Сартировка,цена")
    def filter_test(self, price_1, price_2):
        self.wait.until(EC.element_to_be_clickable(self.FILTER_MENU_SORTED)).click()
        self.wait.until(EC.element_to_be_clickable(self.FILTER_PO_RETING)).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.PRICE)).click()

        input_1 = self.wait.until(EC.element_to_be_clickable(self.PRECE_INPUT_1))
        input_1.click()
        input_1.send_keys(price_1)

        input_2 = self.wait.until(EC.element_to_be_clickable(self.PRECE_INPUT_2))
        input_2.click()
        input_2.send_keys(price_2)

    @allure.step("Заполнение фильтра цена негативный сценарий")
    def filter_test_negative(self, arg1, arg2, fill_both):
        self.wait.until(EC.element_to_be_clickable(self.FILTER_MENU_SORTED)).click()
        self.wait.until(EC.element_to_be_clickable(self.FILTER_PO_RETING)).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.PRICE)).click()
        input_1 = self.wait.until(EC.element_to_be_clickable(self.PRECE_INPUT_1))
        input_1.click()
        input_1.send_keys(arg1)
        border_color_input_1 = input_1.value_of_css_property("border-color")
        if fill_both:
            assert border_color_input_1 == "rgb(224, 224, 224)", "Цвет рамки input_1 не соответствует ожидаемому"
        if fill_both:
            input_2 = self.wait.until(EC.element_to_be_clickable(self.PRECE_INPUT_2))
            input_2.click()
            input_2.send_keys(arg2)
            border_color_input_2 = input_2.value_of_css_property("border-color")
            assert border_color_input_2 == "rgb(239, 83, 80)", "Цвет рамки input_2 не соответствует ожидаемому"


