import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.ShopingPages import *

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_inet_shoping(browser):
    # Открываем сайт магазина
    browser.get("https://www.saucedemo.com/")
    
    # Авторизуемся
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    # Дожидаемся загрузки страницы с товарами
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ProductsPage.ADD_TO_CART_BACKPACK))

    # Добавляем товары в корзину
    products_page = ProductsPage(browser)
    products_page.add_products_to_cart()

    # Дожидаемся загрузки страницы чекаута
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(CheckoutPage.CHECKOUT_BUTTON))

    # Проходим чекаут
    checkout_page = CheckoutPage(browser)
    checkout_page.proceed_to_checkout()

    # Дожидаемся загрузки страницы с формой
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(CheckoutPage.CONTINUE_BUTTON))

    # Заполняем форму
    checkout_page.fill_checkout_form("Фарит", "Шамгулов", "352905")

    # Дожидаемся загрузки страницы с итогами
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(CheckoutPage.TOTAL_PRICE_LABEL))

    # Получаем итоговую сумму и выводим в консоль
    total_price = checkout_page.get_total_price()
    print(f'Итоговая сумма: {total_price}')

    # Завершаем работу с корзиной
    checkout_page.finish_checkout()

    # Переходим на страницу товаров
    checkout_page.go_back_to_products()

    # Проверка итоговой суммы
    assert total_price == "Total: $58.29"