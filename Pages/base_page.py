from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage:
    """
    Базовый класс содержащий функционал для работы с браузером
    """
    def __init__(self, driver):
        self.driver = driver

    def go_to(self, link):
        """
        Открывает страницу

        :param link: ссылка на страницу которая будет открыта
        :return:
        """
        self.driver.get(link)

    def get_element(self, xpath):
        """
        Находит и возвращает веб элемент на текущей странице по xpath если таковой был найден.

        :param xpath: xpath элемента который нужно найти
        :return: WebElement если он был найден, иначе None
        """
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            element = None
        return element

    def get_several_elements(self, xpath) -> list:
        """
        Находит и возвращает все веб элементы на текущей странице по xpath

        :param xpath: xpath элементов которые нужно найти
        :return: List состоящий из найденных WebElement
        """
        elements = self.driver.find_elements(by=By.XPATH, value=xpath)
        return elements

    def send_value(self, xpath, value):
        """
        Вводит данные (value) в веб элемент по xpath.

        :param xpath: xpath к элементу в который нужно ввести данные
        :param value: данные которые будут введены
        :return:
        """
        element = self.get_element(xpath)
        element.send_keys(value)

    def send_action_keys(self, keys):
        """
        Отправляет в браузер нажатие кнопок на клавиатуре

        :param keys: кнопки нажатие которых будет отправлено в браузер
        :return:
        """
        actions = ActionChains(self.driver)
        actions.send_keys(keys)
        actions.perform()

    def click_element(self, xpath):
        """
        Кликает на элемент найденный по переданному xpath

        :param xpath: xpath к элементу на который нужно кликнуть
        :return:
        """
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

    def switch_to_tab_by_number(self, tab_number):
        """
        Меняет активную вкладку для драйвера по переданному номеру

        :param tab_number: порядковый номер вкладки, которую нужно установить активной
        (0 - первая вкладка. Для последней можно передать -1)
        :return:
        """
        self.driver.switch_to.window(self.driver.window_handles[tab_number])

    def get_current_url(self):
        """
        Возвращает url текущей активной вкладки

        :return:
        """
        return self.driver.current_url

    def get_element_text(self, xpath):
        """
        Возвращает текст элемента по xpath

        :param xpath: xpath к элементу текст которого нужно получить
        :return: текст элемента
        """
        element = self.get_element(xpath)
        return element.text

    def get_element_attribute(self, xpath, attr='value'):
        """
        Возвращает значение атрибута элемента по xpath

        :param attr: определяет какой аттрибут элемента нужно получить
        :param xpath: xpath к элементу аттрибут которого нужно получить
        :return: значение запрошенного атрибута
        """
        element = self.get_element(xpath)
        return element.get_attribute(attr)


