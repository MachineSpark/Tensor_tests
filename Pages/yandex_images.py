import time
from selenium.webdriver.common.keys import Keys
from Pages.base_page import BasePage
from Resources.locators import Locators
from Resources import config


class YandexImages(BasePage):
    """
    PageObject класс для тестов связанных с категорией "Картинки" yandex.
    """
    def __init__(self, driver):
        super().__init__(driver)

    def open_search_page(self):
        """
        Открывает главную страницу поиска

        :return:
        """
        self.go_to(config.url_yandex_search)

    def is_images_exist(self):
        """
        Возвращает WebElement раздела "Картинки" (если таковой был найден)

        :return:
        """
        return self.get_element(Locators.link_images)

    def move_to_images(self):
        """
        Выполняет переход в раздел картинки и устанавливает последнюю вкладку
        (новая вкладка открывается при переходе в раздел) в качестве активной

        :return:
        """
        self.click_element(Locators.link_images)
        self.switch_to_tab_by_number(-1)

    def is_on_images_screen(self):
        """
        Проверяет находиться ли браузер на странице раздела Картинки путем проверки url

        :return: bool
        """
        url = self.get_current_url()
        if config.url_yandex_images in url:
            return True     # На странице раздела Картинки
        else:
            return False    # Не на странице раздела Картинки

    def enter_n_category(self, category_number: int):
        """
        Открывает категорию картинок под порядковым номером согласно переданному category_number

        :param category_number: порядковый номер категории, который нужно открыть
        :return: название категории на которую был совершен клик
        """
        category_xpath = Locators.n_category_images(category_number)
        category_text = self.get_element_text(category_xpath)
        self.click_element(category_xpath)
        return category_text

    def is_search_success(self):
        """
        Возвращает WebElement для результата поиска в категории Картинки (если таковой был найден)

        :return:
        """
        return self.get_element(Locators.image_search_results)

    def get_search_text(self):
        """
        Возвращает текущий текст из поля поиска

        :return:
        """
        return self.get_element_attribute(Locators.search)

    def open_n_image(self, image_number, load_timeout=3):
        """
        Открывает картинку из результатов поиска под порядковым номером согласно переданному image_number

        :param image_number: порядковый номер картинки, которую нужно открыть
        :param load_timeout: таймаут, что бы дать яндексу прогрузить ссылки на картинки
        :return:
        """
        self.click_element(Locators.n_image(image_number))
        time.sleep(load_timeout)

    def is_image_open(self):
        """
        Возвращает WebElement для открытой картинки (если таковой был найден)

        :return:
        """
        return self.get_element(Locators.opened_image)

    def get_opened_image_link(self):
        """
        Возвращает ссылку на текущую открытую картинку

        :return:
        """
        return self.get_element_attribute(Locators.opened_image, attr='src')

    def next_image_by_keyboard(self):
        """
        Переходит на следующую картинку путем нажатия на правую стрелку на клавиатуре

        :return:
        """
        time.sleep(0.5)     # без задержки есть шанс, что яндекс проигнорирует нажатие
        self.send_action_keys(Keys.ARROW_RIGHT)

    def previous_image_by_keyboard(self):
        """
        Переходит на предыдущую картинку путем нажатия на левую стрелку на клавиатуре

        :return:
        """
        time.sleep(0.5)     # без задержки есть шанс, что яндекс проигнорирует нажатие
        self.send_action_keys(Keys.ARROW_LEFT)
