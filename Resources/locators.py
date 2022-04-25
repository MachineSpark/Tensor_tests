class Locators:
    """Xpath используемые для теста"""
    search = "//form[@role='search']//input[@name='text']"
    search_suggest = "//ul[contains(@id, 'suggest-list')]"
    search_results = "//ul[@id='search-result']"

    @staticmethod
    def link_in_first_n_search_results(amount: int, link: str):
        """
        Возвращает xpath проверяющий наличие ссылки в определенном количестве первых результатов поиска
        :param amount: в каком кол-ве результатов поиска нужно искать ссылку (от 0 до amount)
        :param link: ссылка наличие которой нужно проверить
        :return:
        """
        return f"//ul[@id='search-result']//li[position()<={amount}]//b[text()='{link}']"

    link_images = "//a[@data-id='images']"

    @staticmethod
    def n_category_images(n: int):
        """
        Возвращает xpath ведущей к определенной по номеру категории картинок
        :param n: порядковый номер категории картинок
        :return:
        """
        return f"(//div[@class='PopularRequestList']//div[contains(@class, 'PopularRequestList-SearchText')])[{n}]"

    image_search_results = "//div[text()='Картинки']/ancestor::a[contains(@class, 'tab_selected_yes')]" \
                           "//following::div[(@role='main')]"

    @staticmethod
    def n_image(n: int):
        """
        Возвращает xpath ведущей к определенной картинке из результатов поиска картинок
        :param n: порядковый номер картинки
        :return:
        """
        return f"(//div[contains(@class, 'content') and @role='main']//div[@role='list']//div[@role='listitem'])[{n}]"

    opened_image = "//div[contains(@class, 'Modal_visible')]//img[@class='MMImage-Preview']"
