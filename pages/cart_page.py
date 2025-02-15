
import allure
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    PAGE_URL = Links.KEIS

    CLASS = (By.CSS_SELECTOR,
             "#content > div > div > div.reducer___VlXNR > div.content___bYv7r.content___Mr05j > main > div > div > div:nth-child(2) > div > div > div:nth-child(2) > div > div > div > div > div > div:nth-child(2) > div.variants___n9U3A > div > div > ul > li:nth-child(2) > span > label > div.border___tFzXN")
    CART_BUTTON = (By.CSS_SELECTOR,
                   "#content > div > div > div.reducer___VlXNR > div.content___bYv7r.content___Mr05j > main > div > div > div:nth-child(2) > div > div > div:nth-child(2) > div > div > div > div > div > div.card___dYHq0 > div.priceRow___Y_JMX > div > div.buttons___sj215.buttonsColumn___boUKs > div > div > div > button")
    PRODUCT = (By.CSS_SELECTOR,
               "#content > div > div > div.reducer___VlXNR > div.content___bYv7r.content___Mr05j > main > div > div > div:nth-child(2) > div > div > div:nth-child(2) > div > div > div > div > div > div:nth-child(2) > div.variants___n9U3A > div:nth-child(3) > div > ul > li:nth-child(1) > span > label")
    CART_PRODUCT = (By.CSS_SELECTOR,
                    "#content > div > div > div.reducer___VlXNR > div.header___tpejM.mobileSticky___MPlWZ > div > div > div > div > div:nth-child(4) > div > div:nth-child(4) > div > a > div > div.headerButtonIcon___pfQ4S > span")

    NAME_PRODUCT = (By.CSS_SELECTOR,
                    "#content > div > div > div.reducer___VlXNR > div.content___bYv7r.content___Mr05j > main > div > div > div:nth-child(2) > div > div > div:nth-child(2) > div > div > div > div > div > div.card___dYHq0 > div.nameRow___f1MUM > h1")

    NAME_PRODUCT_CART = (By.CSS_SELECTOR, "label[for='cartitem-676a59c3c20e570b5baa77c7']")

    CART = (By.CSS_SELECTOR,
            "#content > div > div > div.reducer___VlXNR > div.header___tpejM.mobileSticky___MPlWZ > div > div > div > div > div:nth-child(4) > div > div:nth-child(4) > div > a > div > div.headerButtonIcon___pfQ4S")

    BUTTON_BUY = (By.CSS_SELECTOR,
                  "#content > div > div > div.reducer___VlXNR > div.content___bYv7r > main > div.reducer___QiVrb.center____hfUB.noMarginBottom___N4xR2 > div > div > div.column___xuuui.marginBottom___pgECc.md-4___RMKMP > div > div > div > div > div.whiteList___EskNB > div > div > div:nth-child(5) > div > button")
    STATE_INPUT = (By.NAME, 'state')
    CITY_INPUT = (By.NAME, 'city')
    STREET_INPUT = (By.NAME, 'street')
    HOUSE_INPUT = (By.NAME, 'house')
    APARTAMENT = (By.NAME, 'flat')
    INDEX = (By.NAME, 'zip')
    BUTTON = (By.CSS_SELECTOR,
              "#content > dialog > div.design___DhENZ.designPopup___DVpuO > div > form > div.overlay___l81pO > div > div > button")
    LAST_NAME_INPUT = (By.NAME, 'lastName')
    FIRST_NAME_INPUT = (By.NAME, 'firstName')
    PHONE_INPUT = (By.NAME, 'phone')
    EMAIL_INPUT = (By.NAME, 'email')
    SAVE_BUTTON = (By.CSS_SELECTOR, "#content > dialog > div.design___DhENZ.designPopup___DVpuO > div > form > div.overlay___l81pO > div > div > button")

    @allure.step("Проверка добавлен ли товар в корзину")
    def check_product(self):
        try:
            self.driver.execute_script("window.scrollBy(0, 100)")
            self.wait.until(EC.visibility_of_element_located(self.CLASS)).click()
            self.wait.until(EC.visibility_of_element_located(self.PRODUCT)).click()
            self.wait.until(EC.visibility_of_element_located(self.CART_BUTTON)).click()
            self.wait.until(EC.visibility_of_element_located(self.CART_PRODUCT)).click()
        except:
            assert False, "Товар отсутвует в корзине"

    @allure.step("Переходим в корзину и сравниваем товар")
    def check_cart(self):
        name_product_txt = self.find(self.NAME_PRODUCT).text
        self.check_product()
        print(2)
        element = self.wait.until(
            EC.presence_of_element_located(self.NAME_PRODUCT_CART)
        )
        name_product_cart_txt = element.text

        decoded_string1 = name_product_txt.encode().decode('utf-8').split()
        decoded_string2 = name_product_cart_txt.encode().decode('utf-8').split()

        assert decoded_string2[:10] == decoded_string1[:10]
        self.wait.until(EC.visibility_of_element_located(self.CART)).click()
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_BUY)).click()

    @allure.step("Оформление заказа")
    @allure.title("Тест иногда может падать из за рандомного всплывания рекламы ,после перезапуска тест не падает")
    def registration_order(self):
        self.check_cart()
        self.wait.until(EC.element_to_be_clickable(self.STATE_INPUT)).send_keys("Еврейская Аобл")
        self.wait.until(EC.visibility_of_element_located(self.CITY_INPUT)).send_keys("Биробиджан")
        self.wait.until(EC.visibility_of_element_located(self.STREET_INPUT)).send_keys("ул Парковая")
        self.wait.until(EC.visibility_of_element_located(self.HOUSE_INPUT)).send_keys("2А")
        self.wait.until(EC.visibility_of_element_located(self.APARTAMENT)).send_keys("29")
        self.wait.until(EC.visibility_of_element_located(self.INDEX)).send_keys("679017")
        self.wait.until(EC.visibility_of_element_located(self.BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_INPUT)).send_keys("Иванов")
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT)).send_keys("Иван")
        self.wait.until(EC.visibility_of_element_located(self.PHONE_INPUT)).send_keys("9246454587")
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys("chelovek@mail.ru")
        self.wait.until(EC.visibility_of_element_located(self.SAVE_BUTTON)).click()
        self.get_screenshot()
