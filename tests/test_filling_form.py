import pytest
from pages.filling_form_page import FillingFormPage
import data
import allure
from conftest import driver

class TestFillingForm:

    @allure.title('Заполнение формы заказа')
    @pytest.mark.parametrize(*data.data_for_filling)
    def test_filling_form_data(self, data, driver):
        filling_form = FillingFormPage(driver)
        filling_form.click_top_order_button()
        filling_form.fill_first_name(data["first_name"])
        filling_form.fill_last_name(data["last_name"])
        filling_form.fill_address(data["address"])
        filling_form.fill_phone_number(data["phone_number"])
        filling_form.fill_metro_station(data["metro_station"])
        filling_form.click_next_button()
        filling_form.fill_when_delivery_field(data["delivery_date"])
        filling_form.fill_rental_period_field(data["rental_period"])
        filling_form.click_order_button()
        filling_form.click_yes_button()
        text = filling_form.success_banner()
        assert 'Заказ оформлен' in text

