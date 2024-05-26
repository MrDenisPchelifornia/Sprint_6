from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import data

class FillingForm:

    next_button = (By.CLASS_NAME, "Button_Button__ra12g.Button_Middle__1CSJM")
    when_delivery_field = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div/input")
    rental_period_field = (By.CLASS_NAME, 'Dropdown-placeholder')
    order_button = (By.XPATH, "/html/body/div/div/div[2]/div[3]/button[2]")
    yes_button = (By.XPATH, "/html/body/div/div/div[2]/div[5]/div[2]/button[2]")
    first_name_field_locator = (By.XPATH, "//div[2]/div[2]/div[1]/input")
    # first_name_field_locator = (By.CLASS_NAME "Input_Input__1iN_Z.Input_Error__1Tx5.Input_Responsible__1jDKN")
    # last_name_field = (By.XPATH, "//div[2]/div[2]/div[2]/input")
    last_name_field = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    # address_field = (By.XPATH, "//div[2]/div[2]/div[3]/input")
    address_field = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    # phone_number_field = (By.XPATH, "//div[2]/div[2]/div[5]/input")
    phone_number_field = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')
    metro_station_field = (By.CLASS_NAME, "select-search__input")
    # metro_station_final_choice =
    # rental_period_final_choice =
    text_on_success_banner = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')

    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = FillingForm.first_name_field_locator
        self.last_name_field = FillingForm.last_name_field
        self.address_field = FillingForm.address_field
        self.phone_number_field = FillingForm.phone_number_field
        self.metro_station_field = FillingForm.metro_station_field

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
        # не успел подумать как сунуть в локатор отдельн
        self.driver.find_element(By.XPATH, f"//*[/html/body/div/div/div[2]/div[2]/div[4]/div/div/input]//div[contains(text(), '{metro_station}')]").click()
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()
    def fill_when_delivery_field(self, delivery_date):
        self.driver.find_element(*self.when_delivery_field).send_keys(delivery_date)
    def fill_rental_period_field(self, rental_period):
        self.driver.find_element(*self.rental_period_field).click()
        # не успел подумать как сунуть в локатор отдельно
        self.driver.find_element(By.XPATH, f"//*[/html/body/div/div/div[2]/div[2]/div[2]/div/div[1]]//div[contains(text(), '{rental_period}')]").click()
    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()
    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

    # def step_filling_first_screen(self, data)

