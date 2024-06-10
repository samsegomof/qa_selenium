import pytest
from selenium import webdriver
import chromedriver_autoinstaller


@pytest.fixture(scope='session')
def browser():
    """
    Фикстура для настройки веб-драйвера Chrome на время тестовой сессии.
    Открывает браузер, переходит на указанный URL и максимизирует окно браузера.
    Возвращает:
        WebDriver: Настроенный и открытый веб-драйвер Chrome.
    """
    url = 'https://sbis.ru/'
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()
