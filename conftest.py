from Resources import config
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='session')
def get_latest_driver():
    """
    Автоматически скачивает актуальную версию chromedriver

    :return: путь к драйверу
    """
    d_path = ChromeDriverManager(path=config.webdrivers_folder).install()
    return d_path


@pytest.fixture()
def init_driver(get_latest_driver, request):
    """
    Создает Webdriver для использования в тестах и закрывает его по их завершению
    """
    service = Service(get_latest_driver)
    driver = webdriver.Chrome(service=service)
    request.cls.driver = driver
    yield
    driver.quit()
