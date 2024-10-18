import pytest
from selenium import webdriver
from page_object.data import URLS


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def driver_main(driver):
    driver.get(URLS['main_page_url'])
    return driver


@pytest.fixture
def driver_order(driver):
    driver.get(URLS['order_page_url'])
    return driver
