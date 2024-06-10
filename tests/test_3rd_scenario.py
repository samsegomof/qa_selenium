from pages.sbis_home_page import SbisHomePage


def test_3rd_scenario(browser):
    """
    Третий тестовый сценарий:
        1) Перейти на https://sbis.ru/
        2) В Footer'e найти и перейти "Скачать локальные версии"
        3) Скачать СБИС Плагин для windows, веб-установщик в папку с данным тестом
        4) Убедиться, что плагин скачался
        5) Сравнить размер скачанного файла в мегабайтах. Он должен совпадать с указанным на сайте
    """
    sbis_home_page = SbisHomePage(browser)

    sbis_download_page = sbis_home_page.go_to_download_sbis()

    sbis_download_page.click_sbis_plugin_tab()

    sbis_download_page.download_sbis_plugin()

    sbis_download_page.sbis_plugin_is_downloaded()

    sbis_download_page.plugin_size_is_correct()
