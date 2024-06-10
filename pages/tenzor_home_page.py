from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.tenzor_about_page import TenzorAboutPage
from pages.base_page import BasePage
from logger_setup import Logger

logger = Logger(__name__).get_logger()


class TenzorHomePage(BasePage):
    """
    Класс главной страницы Tensor, наследует BasePage и содержит методы для взаимодействия с элементами главной страницы.
    Локаторы:
        PEOPLE_STRENGTH_TITLE: Локатор для заголовка блока "Сила в людях".
        TENSOR_ABOUT_LINK: Локатор для ссылки на страницу "О компании".
    """

    PEOPLE_STRENGTH_TITLE = (By.XPATH, '//div[contains(@class, "tensor_ru-Index__block4-content")]/p[1]')
    TENSOR_ABOUT_LINK = (By.XPATH, '//a[@href="/about" and contains(@class, "tensor_ru-link")]')

    def url_is_valid(self):
        """
        Проверяет, что URL текущей страницы соответствует URL главной страницы Tensor.
        """

        tenzor_url ='https://tensor.ru/'

        tenzor_url_valid = WebDriverWait(self.driver, 10).until(
            ec.url_to_be(tenzor_url)
        )

        assert tenzor_url_valid

        logger.info('По ссылке "Подробнее" открывается верная страница.')

    def people_strength_block_is_presented(self):
        """
        Проверяет, что блок "Сила в людях" присутствует на странице.
        """

        title = 'Сила в людях'

        block_is_presented = WebDriverWait(self.driver, 10).until(
            ec.text_to_be_present_in_element(self.PEOPLE_STRENGTH_TITLE, title)
        )

        assert block_is_presented

        logger.info('Блок Сила в людях есть на странице.')

    def go_to_tensor_about(self) -> TenzorAboutPage:
        """
        Переходит на страницу "О компании" по ссылке.
        Возвращает:
            TenzorAboutPage: Объект страницы "О компании".
        """

        url = self.get_url_by_locator(self.TENSOR_ABOUT_LINK)
        self.open(url)

        logger.info('Переход по ссылке Подробнее.')

        return TenzorAboutPage(self.driver)
