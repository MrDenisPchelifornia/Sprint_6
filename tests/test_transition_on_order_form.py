from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.scooter_main_page import ScooterMainPage
from locators.scooter_main_locators import ScooterMainLocators

class TestTransitionOnOrderForm:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_transition_through_top_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_screen = ScooterMainPage(self.driver)
        main_screen.click_on_order_button_top()
        assert self.driver.find_element(*ScooterMainLocators.for_who_scotter_hader_on_main).text == 'Для кого самокат'

    def test_transition_through_bottom_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_screen = ScooterMainPage(self.driver)
        main_screen.skip_cookie_banner_batton()
        main_screen.scroll_and_click_on_order_button_bottom()
        assert self.driver.find_element(*ScooterMainLocators.for_who_scotter_hader_on_main).text == 'Для кого самокат'

    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()

