# Sprint_6
# Яндекс Самокат

**URL:** [Яндекс Самокат](https://qa-scooter.praktikum-services.ru/)

**Описание:**  
Яндекс Самокат — это веб-приложение, позволяющее пользователям заказывать самокаты.

**Автоматизированные тесты:**  
В проекте реализованы автоматизированные тесты, направленные на проверку функциональности приложения. Тесты написаны с использованием фреймворка **pytest** и библиотеки **Selenium** для взаимодействия с веб-страницами.

**Стек технологий:**
- Python
- pytest
- Selenium
- Git

### Структура проекта:

- **README.md**: Документация проекта, содержащая описание и инструкции.
- **conftest.py**: Файл с фикстурами, используемыми в тестах для подготовки окружения.
- **data.py**: Хранит данные, используемые в тестах.
- **helpers.py**: Вспомогательные функции для тестирования.
- **requirements.txt**: Список зависимостей проекта.

- **page_object/**: Директория с файлами, описывающими элементы страниц и действия на них.
  - **locators/**: Локаторы для элементов на страницах.
    - main_page_locators.py
    - order_page_locators.py
  - **pages/**: Страницы приложения.
    - base_page.py
    - main_page.py
    - order_page.py
  - **tests/**: Тесты для различных функций приложения.
    - test_main_page.py
    - test_order_page.py
    - test_redirects.py

**Описание тестов:**
- **Тесты главной страницы:** 
  - `test_answer_corresponds_to_question`: Проверяет, что при клике на вопрос отображается соответствующий ответ из списка.
  - `test_open_order_form_via_top_button`: Проверяет, что при нажатии на верхнюю кнопку "Заказать" открывается форма заказа.
  - `test_open_order_form_via_bottom_button`: Проверяет, что при нажатии на нижнюю кнопку "Заказать" открывается форма заказа.

- **Тесты страницы заказа:** 
  - `test_create_order`: Проверяет создание заказа, заполняя форму с данными пользователя и подтверждая заказ.

- **Тесты редиректов:** 
  - `test_open_main_page_by_scooter_logo_click`: Проверяет, что по клику на логотип самоката открывается главная страница.
  - `test_open_dzen_main_page_by_yandex_logo_click`: Проверяет, что по клику на логотип Яндекса открывается главная страница Дзена.


**Отчеты сгенерированы в папку `allure_results`.**
