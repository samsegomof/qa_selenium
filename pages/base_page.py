from typing import Tuple, List

from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """
        Базовый класс для всех страниц, содержащий общие методы для работы с веб-страницами.

        Атрибуты:
            driver: Веб-драйвер, используемый для взаимодействия с браузером.
    """

    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        """Открывает веб-страницу по указанному URL.
            Аргументы:
                url: URL веб-страницы, которую нужно открыть.
        """

        self.driver.get(url)

    def find(self, locator: Tuple) -> WebElement:
        """Находит элемент на веб-странице по указанному локатору.
            Аргументы:
                locator: Кортеж, содержащий стратегию локатора и значение.
            Возвращает:
                WebElement: Найденный элемент.
        """

        return self.driver.find_element(*locator)

    def find_all(self, locator: Tuple) -> List[WebElement]:
        """Находит все элементы на веб-странице по указанному локатору.
            Аргументы:
                locator: Кортеж, содержащий стратегию локатора и значение.
            Возвращает:
                list[WebElement]: Список найденных элементов.
        """

        return self.driver.find_elements(*locator)

    def click(self, locator: Tuple):
        """Кликает на элемент по указанному локатору.
            Аргументы:
                locator: Кортеж, содержащий стратегию локатора и значение.
        """

        self.find(locator).click()

    def get_url_by_locator(self, locator: Tuple) -> str:
        """Возвращает URL, связанный с элементом по указанному локатору.

        Аргументы:
            locator: Кортеж, содержащий стратегию локатора и значение.

        Возвращает:
            str: URL, связанный с элементом."""

        link = self.find(locator)
        url = link.get_attribute('href')
        return url
