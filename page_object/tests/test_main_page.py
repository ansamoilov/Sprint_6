import allure
import pytest

from page_object.data import ANSWERS
from page_object.pages.main_page import MainPage
from page_object.locators.main_page_locators import MainPageLocators
from page_object.locators.order_page_locators import OrderPageLocators


class TestMainPage:

    @allure.title('Проверка клика на вопросы на главной странице')
    @allure.description('Проверяем, что при клике на вопрос отображается соответствующий ему ответ')
    @pytest.mark.parametrize('question_number', range(len(ANSWERS)))
    def test_answer_corresponds_to_question(self, driver_main, question_number):
        main_page = MainPage(driver_main)
        main_page.click_accept_cookies_button()
        assert main_page.get_answer_text(question_number) == ANSWERS[question_number]

    @allure.title('Проверка открытия формы заказа по кнопке в хедере')
    @allure.description('Проверяем, что при клике на верхнюю копку "Заказать" открывается форма заказа')
    def test_open_order_form_via_top_button(self, driver_main):
        main_page = MainPage(driver_main)
        assert main_page.open_order_form()

    @allure.title('Проверка открытия формы заказа по кнопке под формой заказа')
    @allure.description('Проверяем, что при клике на нижнюю копку "Заказать" открывается форма заказа')
    def test_open_order_form_via_bottom_button(self, driver_main):
        main_page = MainPage(driver_main)
        main_page.click_accept_cookies_button()
        assert main_page.open_order_form_via_bottom_button()
