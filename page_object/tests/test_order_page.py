import allure
import pytest

from page_object.data import CREDENTIALS
from page_object.pages.order_page import OrderPage
from page_object.locators.order_page_locators import OrderPageLocators


class TestOrderPage:

    @allure.title('Проверка создания заказа')
    @allure.description('Проверяем полный флоу создания заказа')
    @pytest.mark.parametrize("credentials", CREDENTIALS)
    def test_create_order(self, driver_order, credentials):
        order_page = OrderPage(driver_order)
        order_page.click_accept_cookies_button()
        order_page.first_order_page_fill_out(
            credentials['name'],
            credentials['lastname'],
            credentials['address'],
            credentials['metro_station'],
            credentials['phone']
        )
        order_page.second_order_page_fill_out(color=credentials['color'], comment=credentials['comment'])
        assert order_page.create_and_confirm_order()
