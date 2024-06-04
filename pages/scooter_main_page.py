from locators.scooter_main_locators import ScooterMainLocators
from locators.filling_form_locators import FillingFormLocators
from pages.base import Base
import allure
from conftest import driver

class ScooterMainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Появление списка вопросов')
    def visibility_question(self):
        self.visibility_elements(ScooterMainLocators.last_element_of_question_list)

    @allure.step('Клик по вопросу')
    def click_on_question(self, locator):
        self.find_element(locator).click()

    @allure.step('Получаем текст в списке')
    def get_open_toggle_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Клик на лого по части "Яндекс"')
    def click_on_yandex_logo(self):
        self.find_element(ScooterMainLocators.yandex_logo).click()

    @allure.step('Клик на лого по части "Самокат"')
    def click_on_scooter_logo(self):
        self.find_element(ScooterMainLocators.scooter_logo).click()

    @allure.step('Клик по верхней кнопке "Заказать"')
    def click_top_order_button(self):
        self.find_element(ScooterMainLocators.order_button_top).click()

    @allure.step('Клик по нижней кнопке "Заказать"')
    def click_bottom_order_button(self):
        self.find_element(ScooterMainLocators.order_button_bottom).click()

    @allure.step('Заголвок первого экрана формы')
    def first_order_screen_header(self):
        return self.find_element(FillingFormLocators.order_first_screen_header).text
