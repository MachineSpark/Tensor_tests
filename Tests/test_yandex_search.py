import pytest
from Pages.yandex_search import YandexSearch


@pytest.mark.usefixtures('init_driver')
class Test_YandexSearch:

    def test_yandex_search(self):
        y_search = YandexSearch(self.driver)
        # Зайти на yandex.ru
        y_search.open_search_page()
        # Проверить наличия поля поиска
        assert y_search.is_search_bar_exist(), "На странице не обнаружено поле поиска"
        # Ввести в поиск Тензор
        y_search.enter_search_value('Тензор')
        # Проверить, что появилась таблица с подсказками (suggest)
        assert y_search.is_search_suggest_exist(), "Не обнаружено поле с подсказками поиска (suggest)"
        # При нажатии Enter появляется таблица результатов поиска
        assert y_search.is_search_success(), "Не обнаружена таблица результатов поиска после нажатия Enter"
        # В первых 5 результатах есть ссылка на tensor.ru
        amount = 5
        link = 'tensor.ru'
        assert y_search.is_link_in_first_n_results(amount, link), \
            f"Ссылка '{link}' не обнаружена в первых {amount} результатах"
