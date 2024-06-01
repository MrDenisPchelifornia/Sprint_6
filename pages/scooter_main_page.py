from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators.scooter_main_locators import ScooterMainLocators
from constants import Constants
from .base import Base

class ScooterMainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def skip_cookie_banner_batton(self):
        try:
            self.find_element(ScooterMainLocators.cookie_banner)
            self.click_on_cookie_banner_batton()
        except:
            pass

    def scroll_down_to_question_list(self):
        element = self.find_element(ScooterMainLocators.last_element_of_question_list)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_on_cookie_banner_batton(self):
        self.click(ScooterMainLocators.cookie_banner_batton)

    def click_on_order_button_top(self):
        self.click(ScooterMainLocators.order_button_top)

    def scroll_and_click_on_order_button_bottom(self):
        element = self.find_element(ScooterMainLocators.order_button_bottom)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_on_how_much_toggle(self):
        self.click(ScooterMainLocators.how_much_toggle)

    def click_on_want_a_lot_toggle(self):
        self.click(ScooterMainLocators.want_a_lot_toggle)

    def click_on_how_to_count_toggle(self):
        self.click(ScooterMainLocators.how_to_count_toggle)

    def click_on_right_here_right_now_toggle(self):
        self.click(ScooterMainLocators.right_here_right_now_toggle)

    def click_on_extend_or_finish_early_toggle(self):
        self.click(ScooterMainLocators.extend_or_finish_early_toggle)

    def click_on_what_about_charging_toggle(self):
        self.click(ScooterMainLocators.what_about_charging_toggle)

    def click_on_may_i_cancel_order_toggle(self):
        self.click(ScooterMainLocators.may_i_cancel_order_toggle)

    def click_on_suburban_problems_toggle(self):
        self.click(ScooterMainLocators.suburban_problems_toggle)

    def steps_before_work_with_drop_down_list(self):
        self.skip_cookie_banner_batton()
        self.scroll_down_to_question_list()

    def click_on_yandex_logo(self):
        self.click(ScooterMainLocators.yandex_logo)

    def click_on_scooter_logo(self):
        self.click(ScooterMainLocators.scooter_logo)
