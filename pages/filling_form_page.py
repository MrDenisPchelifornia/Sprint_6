from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import data
from locators.filling_form_locators import FillingFormLocators

class FillingFormPage:

    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = FillingFormLocators.first_name_field_locator
        self.last_name_field = FillingFormLocators.last_name_field
        self.address_field = FillingFormLocators.address_field
        self.phone_number_field = FillingFormLocators.phone_number_field
        self.metro_station_field = FillingFormLocators.metro_station_field

    def fill_first_name(self, first_name):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*self.last_name_field).send_keys(last_name)

    def fill_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    def fill_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def fill_metro_station(self, metro_station):
        self.driver.find_element(*self.metro_station_field).send_keys(metro_station)
        self.driver.find_element(By.XPATH, f"//*[/html/body/div/div/div[2]/div[2]/div[4]/div/div/input]//div[contains(text(), '{metro_station}')]").click()

    def click_next_button(self):
        self.driver.find_element(*FillingFormLocators.next_button).click()

    def fill_when_delivery_field(self, delivery_date):
        self.driver.find_element(*FillingFormLocators.when_delivery_field).send_keys(delivery_date)

    def fill_rental_period_field(self, rental_period):
        self.driver.find_element(*FillingFormLocators.rental_period_field).click()
        self.driver.find_element(By.XPATH, f"//*[/html/body/div/div/div[2]/div[2]/div[2]/div/div[1]]//div[contains(text(), '{rental_period}')]").click()
    def click_order_button(self):
        self.driver.find_element(*FillingFormLocators.order_button).click()

    def click_yes_button(self):
        self.driver.find_element(*FillingFormLocators.yes_button).click()

