from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage
from logger_setup import Logger

logger = Logger(__name__).get_logger()


class TenzorAboutPage(BasePage):
    """
    Класс страницы "О компании" Tensor, наследует BasePage и содержит методы для взаимодействия с элементами страницы.
    Локаторы:
        WORKING_BLOCK_PHOTOS: Локатор для изображений в блоке "Работаем".
    """

    WORKING_BLOCK_PHOTOS = (By.XPATH, '//img[contains(@class, "tensor_ru-About__block3-image")]')

    def url_is_valid(self):
        """
        Проверяет, что URL текущей страницы соответствует URL страницы "О компании".
        Ассерты:
            URL страницы должен быть 'https://tensor.ru/about'.
        """

        url = 'https://tensor.ru/about'

        url_valid = WebDriverWait(self.driver, 10).until(
            ec.url_to_be(url)
        )

        assert url_valid

        logger.info('Успешный переход по адресу tensor.ru/about.')

    def all_photos_are_the_same_size(self):
        """
        Проверяет, что все фотографии в блоке "Работаем" имеют одинаковые размеры.
        Ассерты:
            Ширина и высота всех фотографий должны быть одинаковыми.
        """

        working_block_photos = self.find_all(self.WORKING_BLOCK_PHOTOS)

        width_list = []
        height_list = []

        for photo in working_block_photos:
            width_list.append(photo.get_attribute('width'))
            height_list.append(photo.get_attribute('height'))

        width_set = set(width_list)
        height_set = set(height_list)

        same_width = len(width_set) == 1
        same_height = len(height_set) == 1

        assert same_width and same_height

        logger.info('Размеры фотографий раздела "Работаем" одинаковые.')
