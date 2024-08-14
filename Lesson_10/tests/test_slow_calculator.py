import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import pytest
import allure
from selenium import webdriver
from pages.SlowCalcPage import SlowCalcPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.epic("Calculator")
@allure.title("Нажатие кнопок на калькуляторе")
@allure.description("Нажатие кнопок на калькуляторе, ожидание и проверка результата")
@allure.feature("Тест 1")
@allure.severity(severity_level='normal')
def test_slow_calculator(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    calc_page = SlowCalcPage(browser)

    with allure.step("Установим задержку"):
        calc_page.set_delay('10')

    with allure.step("Нажмем кнопки"):
        for key in ["7", "+", "8", "="]:
            calc_page.click_button(key)
            print(f'Нажата кнопка {key}')

    with allure.step("Ожидание результата"):
        calc_page.wait_for_result("15")

    with allure.step("Получение результата"):
        result = calc_page.get_result()

    with allure.step("Сравнение результата"):
        assert result == "15"