from selenium.webdriver.common.keys import Keys
from Pages.base_page import BasePage
from Resources.locators import Locators
from Resources import config


class YandexSearch(BasePage):
    """
    PageObject класс для тестов связанных с главной страницей поисковика яндекс https://yandex.ru
    """
    def __init__(self, driver):
        super().__init__(driver)

    def open_search_page(self):
        """
        Открывает главную страницу поиска

        :return:
        """
        self.go_to(config.url_yandex_search)

    def is_search_bar_exist(self):
        """
        Возвращает WebElement поля поиска (если таковой был найден)

        :return:
        """
        return self.get_element(Locators.search)

    def enter_search_value(self, search_value):
        """
        Вводит данные в поле поиска

        :param search_value: Данные которые будут введены
        :return:
        """
        self.send_value(Locators.search, search_value)

    def is_search_suggest_exist(self):
        """
        Возвращает WebElement поля с подсказками поиска (если таковой был найден)

        :return:
        """
        return self.get_element(Locators.search_suggest)

    def commit_search(self):
        """
        Отправляет нажатие кнопки Enter на клавиатуре (для выполнения поиска)

        :return:
        """
        self.send_action_keys(Keys.ENTER)

    def is_search_success(self):
        """
        Выполняет поиск по данным находящимся на данный момент в поле поиска, и
        возвращает результат поиска в виде WebElement (если таковой был найден)

        :return:
        """
        self.commit_search()
        return self.get_element(Locators.search_results)

    def is_link_in_first_n_results(self, amount: int, link: str):
        """
        Проверяет есть ли заданная ссылка в первых n результатах поиска

        :param amount: количество результатов поиска (начиная с первого) которое будет проверенно на наличие ссылки
        :param link: ссылка наличие которой будет проверено
        :return:
        """
        element = self.get_element(Locators.link_in_first_n_search_results(amount, link))
        return element

