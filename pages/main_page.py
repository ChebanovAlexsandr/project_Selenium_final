import time

import allure
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    PAGE_URL = Links.MAIN_PEGE

    ALL_GATEGORIES = (By.CSS_SELECTOR,"#content > div > div > div.reducer___VlXNR > div.content___bYv7r > main > div > "
                                      "div.container___oEcGJ.revision___SySqr.maxSixCols___Mdbit.wide___GRn99 > div > "
                                      "div:nth-child(2) > div > div.header___h428l > a.title___FSohz")
    BURGER_MENU = (By.CSS_SELECTOR,"button[class='allCategoriesButton___HtVxU category___hbRCZ'] span")
    MAN = (By.CSS_SELECTOR,"div[class='popup___aSj1O'] div:nth-child(2) a:nth-child(1)")
    PRODUCT = (By.CSS_SELECTOR, '#content > div > div > div.reducer___VlXNR > div.content___bYv7r.content___Q8COV > main > div.reducer___QiVrb.center____hfUB > div > div > div.column___xuuui.marginBottom___pgECc.md-8___qfAsN.lg-9___J20SI > div > div > div > div > div > div.container___oEcGJ.revision___SySqr.narrow___zJbvc > div > div:nth-child(2) > div > a > div.square___Ri5Uw > div > div.imagePlace___sXKA2 > div')
    CART = (By.CSS_SELECTOR, "button[class='button___Fogz2 rounded-rect___bviwL large___rb5cP accent___SFpoh large___rb5cP']")

    @allure.step("Проверка текста")
    def text_verification(self, text):
        self.driver.implicitly_wait(5)
        t = self.find(self.ALL_GATEGORIES)
        assert text == t.text, "Ошибка текст не верный"

    @allure.step("Проверка бургер меню")
    def clock_burger_menu(self):
        burger = self.find(self.BURGER_MENU)
        burger.click()

    @allure.step("Открытие товара в новом окне")
    def click_man(self,text):
        self.wait.until(EC.element_to_be_clickable(self.MAN)).click()
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT)).click()
        tab_2 = self.driver.window_handles[1]
        self.driver.switch_to.window(tab_2)
        t = self.find(self.CART)
        assert text == t.text, "Ошибка текст не верный"



