import pytest
from Pages.yandex_images import YandexImages


@pytest.mark.usefixtures('init_driver')
class Test_YandexImages:

    def test_yandex_images(self):
        y_images = YandexImages(self.driver)
        # 1. Зайти на yandex.ru
        y_images.open_search_page()
        # 2. Ссылка «Картинки» присутствует на странице
        assert y_images.is_images_exist(), "Ссылка на раздел 'Картинки' не обнаружена"
        # 3. Кликаем на ссылку
        y_images.move_to_images()
        # 4. Проверить, что перешли на url https://yandex.ru/images/
        assert y_images.is_on_images_screen() is True, "Текущий URL не содержит https://yandex.ru/images/"
        # 5. Открыть 1 категорию, проверить что открылась, в поиске верный текст
        category_text = y_images.enter_n_category(1)
        assert y_images.is_search_success(), "Не обнаружена таблица с картинками по результатам поиска"
        search_text = y_images.get_search_text()
        assert category_text == search_text, \
            f"Текст в строке поиска не совпадает с текстом категории кликнутой ранее. " \
            f"Текст с категории: '{category_text}'. Текст в строке поиска: '{search_text}'"
        # 6. Открыть 1 картинку, проверить что открылась
        y_images.open_n_image(1)
        assert y_images.is_image_open(), "Не обнаружена открытая картинка"
        # 7. При нажатии кнопки вперед картинка изменяется
        img_link_1 = y_images.get_opened_image_link()
        y_images.next_image_by_keyboard()
        img_link_2 = y_images.get_opened_image_link()
        assert img_link_1 != img_link_2, f"Открытая картинка не изменилась после нажатия ARROW_RIGHT\n" \
                                         f"Картинка 1: '{img_link_1}'\nКартинка 2: '{img_link_2}'"
        # 8. При нажатии кнопки назад картинка изменяется на изображение из шага 6
        y_images.previous_image_by_keyboard()
        img_link_2 = y_images.get_opened_image_link()
        assert img_link_1 == img_link_2, \
            f"Открытая картинка не совпадает с изначально открытой после после возвращения к ней через ARROW_LEFT\n" \
            f"Оригинальная картинка: '{img_link_1}'\nКартинка после возврата: '{img_link_2}'"
