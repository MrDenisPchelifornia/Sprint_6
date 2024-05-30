from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators.scooter_main_locators import ScooterMainLocators
from constants import Constants

class ScooterMainPage:

    def __init__(self, driver):
        self.driver = driver

    def skip_cookie_banner_batton(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(ScooterMainLocators.cookie_banner)
            )
            self.click_on_cookie_banner_batton()
        except TimeoutException:
            pass

    def scroll_down_to_question_list(self):
        element = self.driver.find_element(*ScooterMainLocators.last_element_of_question_list)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_on_cookie_banner_batton(self):
        self.driver.find_element(*ScooterMainLocators.cookie_banner_batton).click()

    def click_on_order_button_top(self):
        self.driver.find_element(*ScooterMainLocators.order_button_top).click()

    def scroll_and_click_on_order_button_bottom(self):
        element = self.driver.find_element(*ScooterMainLocators.order_button_bottom)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_on_how_much_toggle(self):
        self.driver.find_element(*ScooterMainLocators.how_much_toggle).click()

    def click_on_want_a_lot_toggle(self):
        self.driver.find_element(*ScooterMainLocators.want_a_lot_toggle).click()

    def click_on_how_to_count_toggle(self):
        self.driver.find_element(*ScooterMainLocators.how_to_count_toggle).click()

    def click_on_right_here_right_now_toggle(self):
        self.driver.find_element(*ScooterMainLocators.right_here_right_now_toggle).click()

    def click_on_extend_or_finish_early_toggle(self):
        self.driver.find_element(*ScooterMainLocators.extend_or_finish_early_toggle).click()

    def click_on_what_about_charging_toggle(self):
        self.driver.find_element(*ScooterMainLocators.what_about_charging_toggle).click()

    def click_on_may_i_cancel_order_toggle(self):
        self.driver.find_element(*ScooterMainLocators.may_i_cancel_order_toggle).click()

    def click_on_suburban_problems_toggle(self):
        self.driver.find_element(*ScooterMainLocators.suburban_problems_toggle).click()

    def steps_before_work_with_drop_down_list(self):
        self.skip_cookie_banner_batton()
        self.scroll_down_to_question_list()

    def click_on_yandex_logo(self):
        self.driver.find_element(*ScooterMainLocators.yandex_logo).click()

    def click_on_scooter_logo(self):
        self.driver.find_element(*ScooterMainLocators.scooter_logo).click()
