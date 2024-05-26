from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.scooter_main_page import ScooterMain, TransferThroughLogo
from pages.filling_form_page import FillingForm

class TestTransferThroughLogoPart:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_transfer_through_logo_scooter_part(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        transfer = TransferThroughLogo(self.driver)
        transfer.click_on_order_button_top()
        transfer.click_on_scooter_logo()
        assert ('Самокат\n'+'на пару дней\n'+'Привезём его прямо к вашей двери,\n'+'а когда накатаетесь — заберём') in self.driver.find_element(*TransferThroughLogo.home_page_header).text

    def test_transfer_through_logo_yandex_part(self):
        current_window = self.driver.current_window_handle
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        transfer = TransferThroughLogo(self.driver)
        transfer.click_on_yandex_logo()

        for window_handle in self.driver.window_handles:
            if window_handle != current_window:
                self.driver.switch_to.window(window_handle)
                break

        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://dzen.ru/?yredirect=true"))

        assert "https://dzen.ru/?yredirect=true" in self.driver.current_url.lower()

        self.driver.close()
        self.driver.switch_to.window(current_window)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

