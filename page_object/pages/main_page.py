import allure

from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.base_page import BasePage
from page_object.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Клик на принятие cookies')
    def click_accept_cookies_button(self):
        accept_cookies_button = self.find_element_with_wait(MainPageLocators.ACCEPT_COOKIE_BUTTON)
        accept_cookies_button.click()
        self.wait_not_element(accept_cookies_button)

    @allure.step('Клик на вопрос')
    def click_to_question(self, locator_q_formatted):
        self.click_to_element(locator_q_formatted)

    @allure.step('Получаем текст вопроса')
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(
            MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(
            MainPageLocators.ANSWER_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_8)
        self.click_to_question(locator_q_formatted)
        answer = self.get_text_from_element(locator_a_formatted)
        return answer

    @allure.step('Открытие формы заказа')
    def open_order_form(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_TOP)
        self.find_element_with_wait(OrderPageLocators.ORDER_HEADER)
