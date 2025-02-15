import datetime
import os

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10,
                                  poll_frequency=1)  # инициализировали ожидание, poll_frequency временной интервал,
        # в течение которого Selenium снова начинает поиск после последней неудачной попытки

    def open(self):  # Метод для открытия браузера
        with allure.step(f"Отрытие на странице {self.PAGE_URL}"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):  # Метод проверки что открылась та страница которую мы планировали
        with allure.step(f"Отрытие на странице {self.PAGE_URL}"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def get_screenshot(self):
        """Создание скриншота"""
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"

        # Абсолютный путь к папке на рабочем столе
        screenshot_dir = os.path.join(os.path.expanduser("~"),
                                      "C:\\Users\\Kristina\\Desktop\\Скриншоты\\project_Selenium_final", "screenshots")

        # Создаём папку, если её нет
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        # Сохраняем скриншот
        screenshot_path = os.path.join(screenshot_dir, name_screenshot)
        self.driver.save_screenshot(screenshot_path)
        print(f"Скриншот выполнен и сохранён в {screenshot_path}")
