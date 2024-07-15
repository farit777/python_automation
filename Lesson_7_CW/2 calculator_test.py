import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = browser.find_element(By.CSS_SELECTOR, 'input#delay')
    browser.execute_script("arguments[0].setAttribute('value','10')", delay_input)

    buttons = {
        "7": "#calculator > div.keys > span:nth-child(1)",
        "+": "#calculator > div.keys > span:nth-child(4)",
        "8": "#calculator > div.keys > span:nth-child(2)",
        "=": "#calculator > div.keys > span.btn.btn-outline-warning"
    }

    for key, button_id in buttons.items():
        button = browser.find_element(By.CSS_SELECTOR, button_id)
        button.click()
        print(f'Нажата кнопка {key}')

    WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))

    result = browser.find_element(By.CSS_SELECTOR, "#calculator > div.top > div.screen").text
    assert result == "15"
