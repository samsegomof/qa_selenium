import time
import os
import wget

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage
from logger_setup import Logger

logger = Logger(__name__).get_logger()


class SbisDownloadPage(BasePage):
    """
    Класс страницы загрузки СБИС, наследует BasePage
    и содержит методы для взаимодействия с элементами страницы загрузки.
    Локаторы:
        SBIS_PLUGIN_TAB: Локатор для вкладки СБИС Плагин.
        SBIS_DOWNLOAD_PLUGIN_LINK: Локатор для ссылки на скачивание плагина.
    """
    SBIS_PLUGIN_TAB = (By.XPATH, '//div[contains(@class, "controls-TabButtons")]/div[2]')
    SBIS_DOWNLOAD_PLUGIN_LINK = (By.LINK_TEXT, 'Скачать (Exe 7.22 МБ)')

    def click_sbis_plugin_tab(self):
        """
        Кликает на вкладку СБИС Плагин и ждет, пока она станет кликабельной.
        """

        time.sleep(3)

        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.SBIS_PLUGIN_TAB)).click()

        logger.info('Успешный переход на вкладку СБИС Плагин.')

    def download_sbis_plugin(self):
        """
        Загружает плагин СБИС по предоставленной ссылке.
        """

        url = self.get_url_by_locator(self.SBIS_DOWNLOAD_PLUGIN_LINK)
        path = os.getcwd()

        logger.info('Началась загрузка плагина.')

        wget.download(url, out=path)
        print('\n')

    def sbis_plugin_is_downloaded(self):
        """
        Проверяет, что плагин СБИС был успешно загружен.
        """

        current_dir = os.getcwd()

        downloaded_file_name = 'sbisplugin-setup-web.exe'
        downloaded_file_path = current_dir + '/' + downloaded_file_name

        assert os.path.isfile(downloaded_file_path)

        logger.info('Плагин успешно загружен.')

    def plugin_size_is_correct(self):
        """
        Проверяет, совпадает ли размер файла с указанным на сайте.
        """

        current_dir = os.getcwd()

        downloaded_file_name = 'sbisplugin-setup-web.exe'
        downloaded_file_path = current_dir + '/' + downloaded_file_name

        true_file_size = 7.22

        downloaded_file_size = os.path.getsize(downloaded_file_path) / 1048576
        downloaded_file_size = round(downloaded_file_size, 2)

        assert downloaded_file_size == true_file_size
        logger.info('Загруженный плагин имеет верный размер.')
