from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from data import data_for_filling

class FillingFormLocators():

    first_name_field_locator = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    last_name_field = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    address_field = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    phone_number_field = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')
    metro_station_field = (By.CLASS_NAME, "select-search__input")
    next_button = (By.CLASS_NAME, "Button_Button__ra12g.Button_Middle__1CSJM")
    when_delivery_field = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')
    rental_period_field = (By.CLASS_NAME, 'Dropdown-placeholder')
    order_button = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    yes_button = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    text_on_success_banner = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    metro_station_list = (By.XPATH, "//*[/html/body/div/div/div[2]/div[2]/div[4]/div/div/input]//div[contains(text(), '{}')]")
    rental_period_list = (By.XPATH, "//*[/html/body/div/div/div[2]/div[2]/div[2]/div/div[1]]//div[contains(text(), '{}')]")



