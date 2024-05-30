from selenium import webdriver
from selenium.webdriver.common.by import By

class ScooterMainLocators:
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
    how_much_toggle_expect_open = (By.XPATH, "/html/body/div/div/div/div[5]/div[2]/div/div[1]/div[2]/p")
    want_a_lot_toggle_open = (By.XPATH, "/html/body/div/div/div/div[5]/div[2]/div/div[2]/div[2]/p")
    how_to_count_toggle_open = (By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[3]/div[2]/p")
    right_here_right_now_toggle_open = (By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[4]/div[2]/p")
    extend_or_finish_early_toggle_open = (By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[5]/div[2]/p")
    what_about_charging_toggle_open = (By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[6]/div[2]/p")
    may_i_cancel_order_toggle_open = (By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[7]/div[2]/p")
    suburban_problems_toggle_open = (By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[8]/div[2]/p")
    yandex_logo = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    scooter_logo = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    for_who_scotter_hader_on_main = (By.XPATH, "/html/body/div/div/div[2]/div[1]")

    #Локаторы для переходов
    for_who_scotter_hader_on_main = (By.XPATH, "/html/body/div/div/div[2]/div[1]")

    yandex_logo = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    scooter_logo = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

    home_page_header = (By.CLASS_NAME, 'Home_Header__iJKdX')