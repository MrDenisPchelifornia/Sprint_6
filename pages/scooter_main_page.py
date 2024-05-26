from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class ScooterMain:

    order_button_top = (By.CLASS_NAME, 'Button_Button__ra12g')
    order_button_bottom = (By.CSS_SELECTOR, '.Button_Button__ra12g.Button_Middle__1CSJM')
    last_element_of_question_list = (By.ID, 'accordion__heading-7')
    how_much_toggle = (By.ID, 'accordion__heading-0')
    want_a_lot_toggle = (By.ID, 'accordion__heading-1')
    how_to_count_toggle = (By.ID, 'accordion__heading-2')
    right_here_right_now_toggle = (By.ID, 'accordion__heading-3')
    extend_or_finish_early_toggle = (By.ID, 'accordion__heading-4')
    what_about_charging_toggle = (By.ID, 'accordion__heading-5')
    may_i_cancel_order_toggle = (By.ID, 'accordion__heading-6')
    suburban_problems_toggle = (By.ID, 'accordion__heading-7')
    cookie_banner = (By.CLASS_NAME, 'App_CookieConsent__1yUIN')
    cookie_banner_batton = (By.ID, 'rcc-confirm-button')
    #Локаторы ниже переделать
    how_much_toggle_expect_text = ((By.XPATH, "/html/body/div/div/div/div[5]/div[2]/div/div[1]/div[2]/p"),'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')
    how_much_toggle_expect_open = (By.XPATH, "/html/body/div/div/div/div[5]/div[2]/div/div[1]/div[2]/p")
    want_a_lot_toggle_expect_text = ((By.XPATH, "/html/body/div/div/div/div[5]/div[2]/div/div[2]/div[2]/p"), 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')
    want_a_lot_toggle_open = (By.XPATH, "/html/body/div/div/div/div[5]/div[2]/div/div[2]/div[2]/p")
    how_to_count_toggle_expect_text = ((By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[3]/div[2]/p"), 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
    how_to_count_toggle_open = (By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[3]/div[2]/p")
    right_here_right_now_toggle_expect_text = ((By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[4]/div[2]/p"), 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')
    right_here_right_now_toggle_open = (By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[4]/div[2]/p")
    extend_or_finish_early_toggle_expect_text = ((By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[5]/div[2]/p"), 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')
    extend_or_finish_early_toggle_open = (By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[5]/div[2]/p")
    what_about_charging_toggle_expect_text = ((By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[6]/div[2]/p"), 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')
    what_about_charging_toggle_open = (By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[6]/div[2]/p")
    may_i_cancel_order_toggle_expect_text = ((By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[7]/div[2]/p"), 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')
    may_i_cancel_order_toggle_open = (By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[7]/div[2]/p")
    suburban_problems_toggle_expect_text = ((By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[8]/div[2]/p"), 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    suburban_problems_toggle_open = (By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[8]/div[2]/p")

    #Локаторы для переходов
    for_who_scotter_hader_on_main = (By.XPATH, "/html/body/div/div/div[2]/div[1]")

    def __init__(self, driver):
        self.driver = driver

    def skip_cookie_banner_batton(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(self.cookie_banner)
            )
            self.click_on_cookie_banner_batton()
        except TimeoutException:
            pass

    def scroll_down_to_question_list(self):
        element = self.driver.find_element(*self.last_element_of_question_list)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_on_cookie_banner_batton(self):
        self.driver.find_element(*self.cookie_banner_batton).click()

    def click_on_order_button_top(self):
        self.driver.find_element(*self.order_button_top).click()

    def scroll_and_click_on_order_button_bottom(self):
        element = self.driver.find_element(*self.order_button_bottom)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_on_how_much_toggle(self):
        self.driver.find_element(*self.how_much_toggle).click()

    def click_on_want_a_lot_toggle(self):
        self.driver.find_element(*self.want_a_lot_toggle).click()

    def click_on_how_to_count_toggle(self):
        self.driver.find_element(*self.how_to_count_toggle).click()

    def click_on_right_here_right_now_toggle(self):
        self.driver.find_element(*self.right_here_right_now_toggle).click()

    def click_on_extend_or_finish_early_toggle(self):
        self.driver.find_element(*self.extend_or_finish_early_toggle).click()

    def click_on_what_about_charging_toggle(self):
        self.driver.find_element(*self.what_about_charging_toggle).click()

    def click_on_may_i_cancel_order_toggle(self):
        self.driver.find_element(*self.may_i_cancel_order_toggle).click()

    def click_on_suburban_problems_toggle(self):
        self.driver.find_element(*self.suburban_problems_toggle).click()

    def steps_before_work_with_drop_down_list(self):
        self.skip_cookie_banner_batton()
        self.scroll_down_to_question_list()

class TransferThroughLogo:

    yandex_logo = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    scooter_logo = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    order_button_top = (By.CLASS_NAME, 'Button_Button__ra12g')
    home_page_header = (By.CLASS_NAME, 'Home_Header__iJKdX')

    def __init__(self, driver):
        self.driver = driver

    def click_on_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    def click_on_order_button_top(self):
        self.driver.find_element(*self.order_button_top).click()

    def click_on_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

