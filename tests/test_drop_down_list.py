from pages.scooter_main_page import ScooterMainPage
import data
import allure
import pytest
from conftest import driver

class TestDropDownList:

    @pytest.mark.parametrize(*data.data_for_drop_down_list)
    @allure.title('Проверка списка вопросов с выпадающими по клику ответами')
    def test_drop_down_list(self, toggle_locator, text_locator, expected_text, driver):
        main_screen = ScooterMainPage(driver)
        main_screen.skip_cookie()
        main_screen.visibility_question()
        main_screen.click_on_question(toggle_locator)
        actual_text = main_screen.get_open_toggle_text(text_locator)
        assert actual_text == expected_text


