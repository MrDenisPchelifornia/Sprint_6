import pytest
from selenium import webdriver
from data import URL


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(URL)

    yield driver

    driver.quit()