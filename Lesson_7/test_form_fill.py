import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.FormPage import FormPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_form_and_check_validation(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    form_page = FormPage(browser)

    # Данные для заполнения формы
    data = {
        "first_name": "Иван",
        "last_name": "Петров",
        "address": "Ленина, 55-3",
        "email": "test@skypro.com",
        "phone_number": "+7 985 899 99 87",
        "city": "Москва",
        "country": "Россия",
        "job_position": "QA",
        "company": "SkyPro"
    }

    # Заполнение формы
    form_page.fill_form(data)

    # Проверка подсветки полей
    assert browser.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class") == "alert py-2 alert-danger"
    assert browser.find_element(By.ID, "first-name").get_attribute("class") == "alert py-2 alert-success"
    assert browser.find_element(By.ID, "last-name").get_attribute("class") == "alert py-2 alert-success"
    assert browser.find_element(By.ID, "address").get_attribute("class") == "alert py-2 alert-success"
    assert browser.find_element(By.ID, "e-mail").get_attribute("class") == "alert py-2 alert-success"
    assert browser.find_element(By.ID, "phone").get_attribute("class") == "alert py-2 alert-success"
    assert browser.find_element(By.ID, "city").get_attribute("class") == "alert py-2 alert-success"
    assert browser.find_element(By.ID, "country").get_attribute("class") == "alert py-2 alert-success"
    assert browser.find_element(By.ID, "job-position").get_attribute("class") == "alert py-2 alert-success"
    assert browser.find_element(By.ID, "company").get_attribute("class") == "alert py-2 alert-success"

  