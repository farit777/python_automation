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

def test_inet_shoping(browser):
    # Открываем сайт магазина
    browser.get("https://www.saucedemo.com/")

    # Авторизуемся
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # Дожидаемся загрузки страницы с товарами
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))

    # Добавляем товары в корзину
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переходим в корзину
    browser.find_element(By.ID, "shopping_cart_container").click()

    # Дожидаемся загрузки страницы чекаута
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "checkout")))

    # Проходим чекаут
    browser.find_element(By.ID, "checkout").click()

    # Дожидаемся загрузки страницы с формой
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "continue")))

    # Заполняем форму
    browser.find_element(By.ID, "first-name").send_keys("Фарит")
    browser.find_element(By.ID, "last-name").send_keys("Шамгулов")
    browser.find_element(By.ID, "postal-code").send_keys("352905")
    browser.find_element(By.ID, "continue").click()

    # Дожидаемся загрузки страницы с итогами
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label")))

    # Получаем итоговую сумму и выводим в консоль
    total_price = browser.find_element(By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label").text
    print(f'Итоговая сумма: {total_price}')

    # Завершаем работу с корзиной
    browser.find_element(By.ID, "finish").click()

    # Переходим на страницу товаров
    browser.find_element(By.ID, "back-to-products").click()

    # Закрываем браузер
    browser.quit()

    # Проверка итоговой суммы
    assert total_price == "Total: $58.29"