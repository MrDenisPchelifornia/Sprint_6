from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.filling_form_page import FillingFormPage
import data
from locators.filling_form_locators import FillingFormLocators

class TestFillingForm:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize(*data.data_for_filling)
    # в заполнеении формы как буд то можно выделить 1-2 шага
    def test_filling_form_data(self, data):
        self.driver.get("https://qa-scooter.praktikum-services.ru/order")
        filling_form = FillingFormPage(self.driver)
        filling_form.fill_first_name(data["first_name"])
        filling_form.fill_last_name(data["last_name"])
        filling_form.fill_address(data["address"])
        filling_form.fill_phone_number(data["phone_number"])
        filling_form.fill_metro_station(data["metro_station"])
        # filling_form.click_on_right_station()
        filling_form.click_next_button()
        filling_form.fill_when_delivery_field(data["delivery_date"])
        actions = ActionChains(self.driver)
        actions.move_by_offset(0, 0).click().perform()
        filling_form.fill_rental_period_field(data["rental_period"])
        filling_form.click_order_button()
        filling_form.click_yes_button()
        assert 'Заказ оформлен' in self.driver.find_element(*FillingFormLocators.text_on_success_banner).text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()