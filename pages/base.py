from selenium.webdriver.support import expected_conditions as EC
from locators.scooter_main_locators import ScooterMainLocators
from conftest import driver
import allure
from selenium.webdriver.support.wait import WebDriverWait

class Base:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Находим элемент')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    @allure.step('Клик на элемент')
    def click_on_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Соглашение с кукки')
    def skip_cookie(self):
        self.click_on_element(ScooterMainLocators.cookie_banner_batton)

    @allure.step('Элемент видим')
    def visibility_elements(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Ждем URL')
    def wait_for_url(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    @allure.step('Текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('URL после перехода')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])