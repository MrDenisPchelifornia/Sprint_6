from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import data
from locators.filling_form_locators import FillingFormLocators
from pages.base import Base
from pages.scooter_main_page import ScooterMainPage
import allure

class FillingFormPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_field = FillingFormLocators.first_name_field_locator
        self.last_name_field = FillingFormLocators.last_name_field
        self.address_field = FillingFormLocators.address_field
        self.phone_number_field = FillingFormLocators.phone_number_field
        self.metro_station_field = FillingFormLocators.metro_station_field
        self.scooter_main_page = ScooterMainPage(driver)

    @allure.step('Заполняем поле для имени')
    def fill_first_name(self, first_name):
        self.send_keys(self.first_name_field, first_name)

    @allure.step('Заполняем поле для фамилии')
    def fill_last_name(self, last_name):
        self.send_keys(self.last_name_field, last_name)

    @allure.step('Заполняем поле для адреса')
    def fill_address(self, address):
        self.send_keys(self.address_field, address)

    @allure.step('Заполняем поле для телефонного номера')
    def fill_phone_number(self, phone_number):
        self.send_keys(self.phone_number_field, phone_number)

    @allure.step('Указываем станцию метро')
    def fill_metro_station(self, metro_station):
        self.send_keys(FillingFormLocators.metro_station_field, metro_station)
        metro_station_list_locator = FillingFormLocators.metro_station_list[0], FillingFormLocators.metro_station_list[
            1].format(metro_station)
        metro_station_element = self.find_element(metro_station_list_locator)
        metro_station_element.click()

    @allure.step('Клик по кнопке "Далее" в первом экране формы')
    def click_next_button(self):
        self.click(FillingFormLocators.next_button)

    @allure.step('Указываем когда привезти самокат')
    def fill_when_delivery_field(self, delivery_date):
        self.send_keys(FillingFormLocators.when_delivery_field, delivery_date)

    @allure.step('Указываем срок аренды')
    def fill_rental_period_field(self, rental_period):
        self.scooter_main_page.skip_cookie_banner_batton()
        self.click(FillingFormLocators.rental_period_field)
        rental_period_list_locator = FillingFormLocators.rental_period_list[0], FillingFormLocators.rental_period_list[1].format(rental_period)
        rental_period_element = self.find_element(rental_period_list_locator)
        rental_period_element.click()

    @allure.step('Клик по кнопке "Заказать" на втором экране формы')
    def click_order_button(self):
        self.click(FillingFormLocators.order_button)

    @allure.step('Нажимаем "Да" в подтверждающем окне формы')
    def click_yes_button(self):
        self.click(FillingFormLocators.yes_button)
