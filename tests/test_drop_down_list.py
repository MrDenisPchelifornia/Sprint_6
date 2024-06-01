from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from pages.scooter_main_page import ScooterMainPage
import data
from constants import Constants
from selenium.webdriver.support import expected_conditions as EC

class TestDropDownList:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize(*data.data_for_drop_down_list)
    def test_drop_down_list(self, toggle_locator, text_locator, expected_text):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_screen = ScooterMainPage(self.driver)
        main_screen.steps_before_work_with_drop_down_list()
        element_to_click = self.driver.find_element(*toggle_locator)
        self.driver.execute_script("arguments[0].click();", element_to_click)
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(text_locator, expected_text)
        )
        assert self.driver.find_element(*text_locator).text == expected_text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

