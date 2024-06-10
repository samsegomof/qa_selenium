from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.tenzor_home_page import TenzorHomePage
from logger_setup import Logger

logger = Logger(__name__).get_logger()


class SbisContactsPage(BasePage):
    """
    Класс страницы контактов СБИС, наследует BasePage и содержит методы для взаимодействия с элементами страницы.
    Локаторы:
        TENSOR_BANNER: Локатор для баннера Tensor.
        CURRENT_REGION: Локатор для текущего региона.
        NEW_REGION: Локатор для нового региона.
        PARTNERS_LIST: Локатор для списка партнеров.
        PARTNERS_LIST_CITY: Локатор для города в списке партнеров.
    """

    TENSOR_BANNER = (By.CSS_SELECTOR, 'a.sbisru-Contacts__logo-tensor')
    CURRENT_REGION = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
    NEW_REGION = (By.XPATH, '//span[text()="41 Камчатский край"]')
    PARTNERS_LIST = (By.NAME, 'itemsContainer')
    PARTNERS_LIST_CITY = (By.CLASS_NAME, 'sbisru-Contacts-List__city')

    def click_tensor_banner(self) -> TenzorHomePage:
        """
        Кликает по баннеру Tensor и открывает страницу TensorHomePage.
        Возвращает:
            TenzorHomePage: Объект страницы дома Tensor.
        """
        logger.info("Переход по баннеру Tensor")
        url = self.get_url_by_locator(self.TENSOR_BANNER)
        self.open(url)

        return TenzorHomePage(self.driver)

    def region_defined_correct(self):
        """
        Проверяет, что текущий регион правильно определен.
        """

        current_region = 'Республика Башкортостан'
        logger.info(f"Текущий регион правильный: {current_region}")
        current_region_is_right = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.CURRENT_REGION, current_region)
        )

        assert current_region_is_right

    def partners_list_presented_and_visible(self):
        """
        Проверяет, что список партнеров представлен и видим.
        """
        logger.info("Список партнеров представлен и виден")
        presented_and_visible = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PARTNERS_LIST)
        )

        assert presented_and_visible

    def change_region(self):
        """
        Меняет текущий регион на 'Камчатский край'.
        """

        logger.info("Смена текущего региона на 'Камчатский край'")
        current_region = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CURRENT_REGION)
        )

        current_region.click()

        new_region = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.NEW_REGION)
        )

        new_region.click()

    def region_changed_successfully(self):
        """
        Проверяет, что регион успешно изменен.

        """

        region = 'Камчатский край'
        logger.info(f"Проверка успешного изменения региона на: {region}")
        region_is_right = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.CURRENT_REGION, region)
        )

        assert region_is_right

    def partners_list_changed_successfully(self):
        """
        Проверяет, что список партнеров изменен.
        """

        partners_city = 'Петропавловск-Камчатский'
        logger.info(f"Успешное изменение списка партнеров на: {partners_city}")
        partners_list_city_is_right = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.PARTNERS_LIST_CITY, partners_city)
        )

        assert partners_list_city_is_right

    def url_is_correct(self):
        """
        Проверяет, что URL страницы содержит строку '41-kamchatskij-kraj'.
        """

        url_region_string = '41-kamchatskij-kraj'
        logger.info(f"Проверка правильности URL: {url_region_string}")
        correct_url = WebDriverWait(self.driver, 10).until(
            EC.url_contains(url_region_string)
        )

        assert correct_url

    def title_is_correct(self):
        """
        Проверяет, что заголовок страницы содержит строку 'Камчатский край'.
        """
        title_region_string = 'Камчатский край'
        logger.info(f"Проверка правильности заголовка страницы: {title_region_string}")
        correct_title = WebDriverWait(self.driver, 10).until(
            EC.title_contains(title_region_string)
        )

        assert correct_title
