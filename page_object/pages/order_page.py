import random

import allure

from page_object.data import RENTAL_TERMS
from page_object.helpers import generate_random_date
from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Клик на принятие cookies')
    def click_accept_cookies_button(self):
        accept_cookies_button = self.find_element_with_wait(OrderPageLocators.ACCEPT_COOKIE_BUTTON)
        accept_cookies_button.click()
        self.wait_not_element(accept_cookies_button)

    @allure.step('Заполнение инпута имени')
    def name_input_fill_out(self, name):
        name_input = self.driver.find_element(*OrderPageLocators.NAME_INPUT)
        name_input.clear()
        name_input.send_keys(name)

    @allure.step('Заполнение инпута фамилии')
    def lastname_input_fill_out(self, lastname):
        lastname_input = self.driver.find_element(*OrderPageLocators.LASTNAME_INPUT)
        lastname_input.clear()
        lastname_input.send_keys(lastname)

    @allure.step('Заполнение инпута адреса')
    def address_input_fill_out(self, address):
        address_input = self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT)
        address_input.clear()
        address_input.send_keys(address)

    @allure.step('Выбор станции метро')
    def metro_station_selection(self, station_name):
        station_input = self.find_element_with_wait(OrderPageLocators.METRO_STATION_INPUT)
        station_input.click()
        station_input.send_keys(station_name)
        station_locator = self.format_locators(OrderPageLocators.STATION_BUTTON, station_name)
        self.find_element_with_wait(station_locator)
        self.click_to_element(station_locator)

    @allure.step('Заполнение инпута номера телефона')
    def phone_input_fill_out(self, phone):
        phone_input = self.driver.find_element(*OrderPageLocators.PHONE_INPUT)
        phone_input.clear()
        phone_input.send_keys(phone)

    @allure.step('Заполнение первой страницы формы заказа')
    def first_order_page_fill_out(self, name, lastname, address, station_name, phone):
        self.name_input_fill_out(name)
        self.lastname_input_fill_out(lastname)
        self.address_input_fill_out(address)
        self.metro_station_selection(station_name)
        self.phone_input_fill_out(phone)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)
        self.find_element_with_wait(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Заполнение даты')
    def start_date_input_fill_out(self, date):
        start_date_input = self.find_element_with_wait(OrderPageLocators.START_DATE_INPUT)
        start_date_input.click()
        start_date_input.send_keys(date)
        self.click_to_element(OrderPageLocators.SELECTED_DATE)

    @allure.step('Выбор срока аренды')
    def select_random_rental_term(self):
        rental_term = random.choice(RENTAL_TERMS)
        self.click_to_element(OrderPageLocators.RENTAL_TERM_INPUT)
        term_locator = self.format_locators(OrderPageLocators.RENTAL_TERM_OPTION, rental_term)
        self.find_element_with_wait(term_locator).click()

    @allure.step('Выбор цвета самоката')
    def select_color_checkbox(self, color):
        if color.lower() == 'черный':
            checkbox_locator = OrderPageLocators.BLACK_COLOR_CHECKBOX
        else:
            checkbox_locator = OrderPageLocators.GREY_COLOR_CHECKBOX
        checkbox = self.find_element_with_wait(checkbox_locator)
        checkbox.click()
        assert checkbox.is_selected()

    @allure.step('Ввод комментария для курьера')
    def comment_input_fill_out(self, comment=None):
        comment_input = self.find_element_with_wait(OrderPageLocators.COMMENT_INPUT)
        if comment:
            comment_input.send_keys(comment)

    @allure.step('Заполнение второй страницы формы заказа')
    def second_order_page_fill_out(self, color, comment=None):
        date = generate_random_date()
        self.start_date_input_fill_out(date)
        self.select_random_rental_term()
        self.select_color_checkbox(color)
        if comment:
            self.comment_input_fill_out(comment)

    @allure.step('Создание и подтверждение заказа')
    def create_and_confirm_order(self):
        self.click_to_element(OrderPageLocators.CREATE_ORDER_BUTTON)
        confirm_button = self.find_element_with_wait(OrderPageLocators.YES_BUTTON)
        confirm_button.click()
        check_status_button = self.find_element_with_wait(OrderPageLocators.CHECK_STATUS_BUTTON)
        return check_status_button

    @allure.step('Клик на логотип самоката для редиректа')
    def click_on_scooter_logo(self):
        self.click_to_element(OrderPageLocators.SCOOTER_LOGO)
