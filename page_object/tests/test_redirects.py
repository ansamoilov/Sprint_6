import allure
from page_object.data import URLS
from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrderPage


class TestRedirects:

    @allure.title('Проверка редиректа по клику на логотип')
    @allure.description('Проверяем, что по клику на логотип самоката открывается главная')
    def test_open_main_page_by_scooter_logo_click(self, driver_order):
        order_page = OrderPage(driver_order)
        order_page.click_on_scooter_logo()
        order_page.check_url(URLS['main_page_url'])

    @allure.title('Проверка редиректа на главную страницу Дзена')
    @allure.description('Проверяем, что по клику на логотип яндекса открывается главная страница Дзена')
    def test_open_dzen_main_page_by_yandex_logo_click(self, driver_main):
        main_page = MainPage(driver_main)
        main_page.click_on_yandex_logo()
        main_page.switch_browser_tab()
        main_page.check_url(URLS['dzen_main_url'])
