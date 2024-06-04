from locators.filling_form_locators import FillingFormLocators
from pages.base import Base
import allure

class FillingFormPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по верхней кнопке "Заказать"')
    def click_top_order_button(self):
        self.find_element(FillingFormLocators.order_button_top).click()

    @allure.step('Заполняем поле для имени')
    def fill_first_name(self, first_name):
        self.find_element(FillingFormLocators.first_name_field).send_keys(first_name)

    @allure.step('Заполняем поле для фамилии')
    def fill_last_name(self, last_name):
        self.find_element(FillingFormLocators.last_name_field).send_keys(last_name)

    @allure.step('Заполняем поле для адреса')
    def fill_address(self, address):
        self.find_element(FillingFormLocators.address_field).send_keys(address)

    @allure.step('Заполняем поле для телефонного номера')
    def fill_phone_number(self, phone_number):
        self.find_element(FillingFormLocators.phone_number_field).send_keys(phone_number)

    @allure.step('Указываем станцию метро')
    def fill_metro_station(self, metro_station):
        self.find_element(FillingFormLocators.metro_station_field).send_keys(metro_station)
        metro_station_list_locator = FillingFormLocators.metro_station_list[0], FillingFormLocators.metro_station_list[
            1].format(metro_station)
        self.find_element(metro_station_list_locator).click()

    @allure.step('Указываем срок аренды')
    def fill_rental_period_field(self, rental_period):
        self.skip_cookie()
        self.find_element(FillingFormLocators.rental_period_field).click()
        rental_period_list_locator = FillingFormLocators.rental_period_list[0], FillingFormLocators.rental_period_list[
            1].format(rental_period)
        self.find_element(rental_period_list_locator).click()

    @allure.step('Клик по кнопке "Далее" в первом экране формы')
    def click_next_button(self):
        self.find_element(FillingFormLocators.next_button).click()

    @allure.step('Указываем когда привезти самокат')
    def fill_when_delivery_field(self, delivery_date):
        self.find_element(FillingFormLocators.when_delivery_field).send_keys(delivery_date)

    @allure.step('Клик по кнопке "Заказать" на втором экране формы')
    def click_order_button(self):
        self.find_element(FillingFormLocators.order_button).click()

    @allure.step('Нажимаем "Да" в подтверждающем окне формы')
    def click_yes_button(self):
        self.find_element(FillingFormLocators.yes_button).click()

    @allure.step('Уведомление об успешном заказе')
    def success_banner(self):
        return self.find_element(FillingFormLocators.text_on_success_banner).text
