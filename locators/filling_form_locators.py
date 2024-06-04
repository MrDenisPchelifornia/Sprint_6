from selenium.webdriver.common.by import By

class FillingFormLocators():

    first_name_field = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    last_name_field = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    address_field = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    phone_number_field = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')
    metro_station_field = (By.CLASS_NAME, "select-search__input")
    next_button = (By.CLASS_NAME, "Button_Button__ra12g.Button_Middle__1CSJM")
    when_delivery_field = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')
    choose_delivery_date = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--029 " "react-datepicker__day--outside-month']")
    rental_period_field = (By.CLASS_NAME, 'Dropdown-placeholder')
    order_button = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    yes_button = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    text_on_success_banner = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    metro_station_list = (By.XPATH, "//*[//div/input]//div[contains(text(), '{}')]")
    rental_period_list = (By.XPATH, "//div[@class='Dropdown-menu']//div[contains(text(), '{}')]")
    order_button_top = (By.CLASS_NAME, 'Button_Button__ra12g')
    order_first_screen_header = (By.CLASS_NAME, 'Order_Header__BZXOb')




