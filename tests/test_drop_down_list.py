from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.scooter_main_page import ScooterMain, TransferThroughLogo
from pages.filling_form_page import FillingForm

class TestDropDownList:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_how_much_toggle(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_screen = ScooterMain(self.driver)
        main_screen.steps_before_work_with_drop_down_list()
        element_to_click = self.driver.find_element(*main_screen.how_much_toggle)
        self.driver.execute_script("arguments[0].click();", element_to_click)
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(*main_screen.how_much_toggle_expect_text))
        assert self.driver.find_element(*main_screen.how_much_toggle_expect_open).text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    def test_want_a_lot_toggle(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_screen = ScooterMain(self.driver)
        main_screen.steps_before_work_with_drop_down_list()
        element_to_click = self.driver.find_element(*main_screen.want_a_lot_toggle)
        self.driver.execute_script("arguments[0].click();", element_to_click)
        #Нижнюю строчку я бы заменил на ожидание расскрытия т.е. что в классе пропал хайд но чет не могу сообразить надо погуглить
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(*main_screen.want_a_lot_toggle_expect_text))
        assert self.driver.find_element(*main_screen.want_a_lot_toggle_open).text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    #Блоки ниже переписать когда сделаю общий шаг и разберусь с вейт что ждать и оссерт что лучше использовать в локаторе
    def test_how_to_count_toggle(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_screen = ScooterMain(self.driver)
        main_screen.steps_before_work_with_drop_down_list()
        element_to_click = self.driver.find_element(*main_screen.how_to_count_toggle)
        self.driver.execute_script("arguments[0].click();", element_to_click)
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(*main_screen.how_to_count_toggle_expect_text))
        assert self.driver.find_element(*main_screen.how_to_count_toggle_open).text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    def test_right_here_right_now_toggle(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_screen = ScooterMain(self.driver)
        main_screen.steps_before_work_with_drop_down_list()
        element_to_click = self.driver.find_element(*main_screen.right_here_right_now_toggle)
        self.driver.execute_script("arguments[0].click();", element_to_click)
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(*main_screen.right_here_right_now_toggle_expect_text))
        assert self.driver.find_element(*main_screen.right_here_right_now_toggle_open).text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def test_extend_or_finish_early_toggle(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_screen = ScooterMain(self.driver)
        main_screen.steps_before_work_with_drop_down_list()
        element_to_click = self.driver.find_element(*main_screen.extend_or_finish_early_toggle)
        self.driver.execute_script("arguments[0].click();", element_to_click)
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(*main_screen.extend_or_finish_early_toggle_expect_text))
        assert self.driver.find_element(*main_screen.extend_or_finish_early_toggle_open).text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    def test_what_about_charging_toggle(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_screen = ScooterMain(self.driver)
        main_screen.steps_before_work_with_drop_down_list()
        element_to_click = self.driver.find_element(*main_screen.what_about_charging_toggle)
        self.driver.execute_script("arguments[0].click();", element_to_click)
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(*main_screen.what_about_charging_toggle_expect_text))
        assert self.driver.find_element(*main_screen.what_about_charging_toggle_open).text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    def test_may_i_cancel_order_toggle(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_screen = ScooterMain(self.driver)
        main_screen.steps_before_work_with_drop_down_list()
        element_to_click = self.driver.find_element(*main_screen.may_i_cancel_order_toggle)
        self.driver.execute_script("arguments[0].click();", element_to_click)
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(*main_screen.may_i_cancel_order_toggle_expect_text))
        assert self.driver.find_element(*main_screen.may_i_cancel_order_toggle_open).text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    def test_suburban_problems_toggle(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_screen = ScooterMain(self.driver)
        main_screen.steps_before_work_with_drop_down_list()
        element_to_click = self.driver.find_element(*main_screen.suburban_problems_toggle)
        self.driver.execute_script("arguments[0].click();", element_to_click)
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(*main_screen.suburban_problems_toggle_expect_text))
        assert self.driver.find_element(*main_screen.suburban_problems_toggle_open).text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()
