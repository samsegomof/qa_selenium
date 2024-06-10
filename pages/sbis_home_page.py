from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.sbis_contacts_page import SbisContactsPage
from pages.sbis_download_page import SbisDownloadPage
from logger_setup import Logger

logger = Logger(__name__).get_logger()


class SbisHomePage(BasePage):
    """
    Класс главной страницы СБИС, наследует BasePage и содержит
    методы для взаимодействия с элементами главной страницы.
    Локаторы:
        CONTACTS_LINK: Локатор для ссылки на страницу контактов.
        SBIS_DOWNLOAD_PAGE_LINK: Локатор для ссылки на страницу загрузки локальных версий.
    """

    CONTACTS_LINK = (By.XPATH, '//a[@href="/contacts" and contains(@class, "sbisru-Footer__link")]')
    SBIS_DOWNLOAD_PAGE_LINK = (By.LINK_TEXT, 'Скачать локальные версии')

    def go_to_contacts_page(self) -> SbisContactsPage:
        """
        Переходит на страницу контактов.
        Возвращает:
            SbisContactsPage: Объект страницы контактов.
        """

        url = self.get_url_by_locator(self.CONTACTS_LINK)
        self.open(url)

        logger.info('Успешный переход в раздел Контакты.')

        return SbisContactsPage(self.driver)

    def go_to_download_sbis(self) -> SbisDownloadPage:
        """
        Переходит на страницу загрузки локальных версий СБИС.
        Возвращает:
            SbisDownloadPage: Объект страницы загрузки локальных версий.
        """

        url = self.get_url_by_locator(self.SBIS_DOWNLOAD_PAGE_LINK)
        self.open(url)

        logger.info('Успешный переход в раздел Скачать.')

        return SbisDownloadPage(self.driver)
