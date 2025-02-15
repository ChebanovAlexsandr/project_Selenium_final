import pytest  # импортируем пайтест для тестов
from selenium import webdriver  # импортируем сам драйвер
from selenium.webdriver.chrome.options import Options  # импортируем для опций драйвера


@pytest.fixture(scope="function", autouse=True)  # Создаёт экземпляр драйвера для каждого теста отдельно
def driver(request):
    options = Options()  # для дополнительных параметор браузера
    # options.add_argument("--headless")     # запуск в безголовом режиме
    options.add_argument("--no-sandbox")  #
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")  # открытие окна по размеру
    driver = webdriver.Chrome(options=options)  # Инициализировали драйвер с параметрами
    request.cls.driver = driver  # request.cls.имя_переменной, в тестовом классе автоматически будет создаваться такой атрибут. Это то же самое, что если бы вы напрямую объявили их в init тестового класса.
    yield driver
    driver.quit()  # закрытие браузера

