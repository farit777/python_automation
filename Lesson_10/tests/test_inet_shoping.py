import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
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

@allure.epic("Shoping")
@allure.title("Отправка товаров в корзину")
@allure.description("Авторизация, добавление товаров в корзину, проверка корзины")
@allure.feature("Тест 1")
@allure.severity(severity_level='normal')
def test_inet_shoping(browser):
    with allure.step("Открываем сайт магазина"):
        browser.get("https://www.saucedemo.com/")
    
    with allure.step("Авторизуемся"):
        login_page = LoginPage(browser)
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Дожидаемся загрузки страницы с товарами"):
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ProductsPage.ADD_TO_CART_BACKPACK))

    with allure.step("Добавляем товары в корзину"):
        products_page = ProductsPage(browser)
        products_page.add_products_to_cart()

    with allure.step("Дожидаемся загрузки страницы чекаута"):
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(CheckoutPage.CHECKOUT_BUTTON))

    with allure.step("Проходим чекаут"):
        checkout_page = CheckoutPage(browser)
        checkout_page.proceed_to_checkout()

    with allure.step("Дожидаемся загрузки страницы с формой"):
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(CheckoutPage.CONTINUE_BUTTON))

    with allure.step("Заполняем форму"):
        checkout_page.fill_checkout_form("Фарит", "Шамгулов", "352905")

    with allure.step("Дожидаемся загрузки страницы с итогами"):
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(CheckoutPage.TOTAL_PRICE_LABEL))

    with allure.step("Получаем итоговую сумму и выводим в консоль"):
        total_price = checkout_page.get_total_price()
        print(f'Итоговая сумма: {total_price}')

    with allure.step("Завершаем работу с корзиной"):
        checkout_page.finish_checkout()

    with allure.step("Переходим на страницу товаров"):
        checkout_page.go_back_to_products()

    with allure.step("Проверка итоговой суммы"):
        assert total_price == "Total: $58.29"