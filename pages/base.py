from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class Base:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Находим элемент')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))

    @allure.step('Клик на элемент')
    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step('Заполнение поля')
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    @allure.step('Получение текста элемента')
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
