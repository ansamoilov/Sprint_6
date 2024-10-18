from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCEPT_COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    QUESTION_LOCATOR = (By.ID, "accordion__heading-{}")
    ANSWER_LOCATOR = (By.XPATH, "//div[@data-accordion-component='AccordionItemPanel' and @id='accordion__panel-{}']")
    QUESTION_LOCATOR_8 = (By.ID, "accordion__heading-7")
    ORDER_BUTTON_TOP = (
        By.XPATH,
        "//button[contains(@class, 'Button_Button') and not(ancestor::div[contains(@class, 'Home_FinishButton')])]"
    )
    ORDER_BUTTON_BOTTOM = (
        By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']"
    )
