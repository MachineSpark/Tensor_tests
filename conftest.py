from Resources import config
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def init_driver(request):
    """
    Создает Webdriver для использования в тестах и закрывает его по их завершению
    """
    service = Service(config.chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    request.cls.driver = driver
    yield
    driver.quit()
