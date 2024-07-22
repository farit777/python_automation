import pytest
from selenium import webdriver
from pages.SlowCalcPage import SlowCalcPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    calc_page = SlowCalcPage(browser)

    # Установим задержку
    calc_page.set_delay('10')

    # Нажмем кнопки
    for key in ["7", "+", "8", "="]:
        calc_page.click_button(key)
        print(f'Нажата кнопка {key}')

    # Ожидание результата
    calc_page.wait_for_result("15")

    # Проверка результата
    result = calc_page.get_result()
    assert result == "15"