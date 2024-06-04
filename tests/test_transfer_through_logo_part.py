from pages.scooter_main_page import ScooterMainPage
from data import URL, URL_DZEN
import allure
from conftest import driver

class TestTransferThroughLogoPart:

    @allure.title('Переход на главную через лого "Самокат"')
    def test_transfer_through_logo_scooter_part(self, driver):
        transfer = ScooterMainPage(driver)
        transfer.click_top_order_button()
        transfer.click_on_scooter_logo()
        transfer.wait_for_url(URL)
        main_url = URL
        assert main_url == transfer.get_current_url()

    @allure.title('Переход на страницу "Дзен" через лого "Яндекс"')
    def test_transfer_through_logo_yandex_part(self, driver):
        transfer = ScooterMainPage(driver)
        transfer.click_on_yandex_logo()
        transfer.switch_to_window()
        transfer.wait_for_url(URL_DZEN)
        dzen_url = URL_DZEN
        assert dzen_url == transfer.get_current_url()
