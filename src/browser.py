import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions

path_to_driver = 'C:/Chromedriver/chromedriver.exe' # это пример пути как нужно указать а так driver нужно скачать от сюда https://googlechromelabs.github.io/chrome-for-testing/ и тут указать путь до него


@pytest.fixture()
def set_up_browser():
    options = ChromeOptions()

    # Создание объекта Service с указанием пути к Chromedriver
    service = Service(executable_path=path_to_driver)

    # Запуск Chrome с указанным сервисом и опциями
    driver = Chrome(service=service, options=options)
    yield driver
    driver.quit()
