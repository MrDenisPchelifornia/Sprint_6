from pages.scooter_main_page import ScooterMainPage
import allure
from conftest import driver

class TestTransitionOnOrderForm:

    @allure.title('Переход к форме заказа через верхнюю кнопку')
    def test_transition_through_top_button(self, driver):
        main_screen = ScooterMainPage(driver)
        main_screen.click_top_order_button()
        text = main_screen.first_order_screen_header()
        assert 'Для кого самокат' in text

    @allure.title('Переход к форме заказа через нижнюю кнопку')
    def test_transition_through_bottom_button(self, driver):
        main_screen = ScooterMainPage(driver)
        main_screen.skip_cookie()
        main_screen.click_bottom_order_button()
        text = main_screen.first_order_screen_header()
        assert 'Для кого самокат' in text
