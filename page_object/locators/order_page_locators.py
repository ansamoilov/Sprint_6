from selenium.webdriver.common.by import By


class OrderPageLocators:
    SCOOTER_LOGO = (By.XPATH, "//a[img[@alt='Scooter']]")
    YANDEX_LOGO = (By.XPATH, "//a[img[@alt='Yandex']]")
    ACCEPT_COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    ORDER_HEADER = (By.XPATH, "//div[contains(@class, 'Order_Header__BZXOb') and text()='Для кого самокат']")
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(., 'Далее')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(., 'Заказать')]")
    STATION_BUTTON = (By.XPATH, "//button[contains(@class, 'Order_SelectOption__82bhS') and contains(., '{}')]")
    START_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_TERM_INPUT = (By.XPATH, "//div[contains(@class, 'Dropdown-control') and contains(., '* Срок аренды')]")
    RENTAL_TERM_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BLACK_COLOR_CHECKBOX = (By.XPATH, "//input[@id='black']")
    GREY_COLOR_CHECKBOX = (By.XPATH, "//input[@id='grey']")
    SELECTED_DATE = (By.CSS_SELECTOR, "div.react-datepicker__day--selected")
    CREATE_ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Button') and contains(@class, 'Button_Middle') and text()='Заказать']"
    )
    YES_BUTTON = (
        By.XPATH, "//button[contains(@class, 'Button_Button') and contains(@class, 'Button_Middle') and text()='Да']"
    )
    CHECK_STATUS_BUTTON = (
        By.XPATH, "//button[contains(@class, 'Button_Button') and contains(text(), 'Посмотреть статус')]"
    )
