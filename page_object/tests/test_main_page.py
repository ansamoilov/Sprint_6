import allure
import pytest

from page_object.data import ANSWERS
from page_object.pages.main_page import MainPage
from page_object.locators.main_page_locators import MainPageLocators
from page_object.locators.order_page_locators import OrderPageLocators


class TestMainPage:

    @allure.description('Проверяем, что при клике на вопрос отображается соответствующий ему ответ')
    @pytest.mark.parametrize('question_number', range(len(ANSWERS)))
    def test_answer_corresponds_to_question(self, driver_main, question_number):
        main_page = MainPage(driver_main)
        main_page.click_accept_cookies_button()
        assert main_page.get_answer_text(question_number) == ANSWERS[question_number]

    @allure.description('Проверяем, что при клике на верхнюю копку "Заказать" открывается форма заказа')
    def test_open_order_form_via_top_button(self, driver_main):
        main_page = MainPage(driver_main)
        main_page.click_to_element(MainPageLocators.ORDER_BUTTON_TOP)
        assert main_page.find_element_with_wait(OrderPageLocators.ORDER_HEADER)

    @allure.description('Проверяем, что при клике на нижнюю копку "Заказать" открывается форма заказа')
    def test_open_order_form_via_top_button(self, driver_main):
        main_page = MainPage(driver_main)
        main_page.click_accept_cookies_button()
        order_button_element = main_page.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        order_button_element.click()
        assert main_page.find_element_with_wait(OrderPageLocators.ORDER_HEADER)
