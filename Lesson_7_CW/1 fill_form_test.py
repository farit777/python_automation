import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_form_and_check_validation(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    first_name = browser.find_element(By.NAME, "first-name")
    first_name.send_keys("Иван")

    last_name = browser.find_element(By.NAME, "last-name")
    last_name.send_keys("Петров")

    address = browser.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")

    email = browser.find_element(By.NAME, "e-mail")
    email.send_keys("test@skypro.com")

    phone_number = browser.find_element(By.NAME, "phone")
    phone_number.send_keys("+7 985 899 99 87")

    city = browser.find_element(By.NAME, "city")
    city.send_keys("Москва")

    country = browser.find_element(By.NAME, "country")
    country.send_keys("Россия")

    job_position = browser.find_element(By.NAME, "job-position")
    job_position.send_keys("QA")

    company = browser.find_element(By.NAME, "company")
    company.send_keys("SkyPro")

    submit_button = browser.find_element(By.CLASS_NAME, "btn.btn-outline-primary")
    submit_button.click()

    # Проверка подсветки полей
    zip_code = browser.find_element(By.CSS_SELECTOR, "#zip-code")
    assert zip_code.get_attribute("class") == "alert py-2 alert-danger"

    first_name = browser.find_element(By.ID, "first-name")
    assert first_name.get_attribute("class") == "alert py-2 alert-success"

    last_name = browser.find_element(By.ID, "last-name")
    assert last_name.get_attribute("class") == "alert py-2 alert-success"

    address = browser.find_element(By.ID, "address")
    assert address.get_attribute("class") == "alert py-2 alert-success"

    email = browser.find_element(By.ID, "e-mail")
    assert email.get_attribute("class") == "alert py-2 alert-success"

    phone_number = browser.find_element(By.ID, "phone")
    assert phone_number.get_attribute("class") == "alert py-2 alert-success"

    city = browser.find_element(By.ID, "city")
    assert city.get_attribute("class") == "alert py-2 alert-success"

    country = browser.find_element(By.ID, "country")
    assert country.get_attribute("class") == "alert py-2 alert-success"

    job_position = browser.find_element(By.ID, "job-position")
    assert job_position.get_attribute("class") == "alert py-2 alert-success"

    company = browser.find_element(By.ID, "company")
    assert company.get_attribute("class") == "alert py-2 alert-success"
