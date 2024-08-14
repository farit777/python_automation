import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    @allure.step("Заполняем поля 'login', 'password' и кликаем по кнопке 'submit'")
    def login(self, username: str, password: str) -> None:
        """
        Заполняет поля 'login', 'password' и кликает по кнопке 'submit'
        """
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

class ProductsPage(BasePage):
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TO_CART_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_TO_CART_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_BUTTON = (By.ID, "shopping_cart_container")

    @allure.step("Находим заданные товары и кликаем по кнопке 'В корзину'")
    def add_products_to_cart(self) -> None:
        """
        Находит заданные товары и кликает по кнопке 'В корзину'
        """
        self.driver.find_element(*self.ADD_TO_CART_BACKPACK).click()
        self.driver.find_element(*self.ADD_TO_CART_TSHIRT).click()
        self.driver.find_element(*self.ADD_TO_CART_ONESIE).click()
        self.driver.find_element(*self.CART_BUTTON).click()

class CheckoutPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_PRICE_LABEL = (By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    BACK_TO_PRODUCTS_BUTTON = (By.ID, "back-to-products")

    @allure.step("Находим кнопку проверки корзины и кликаем по ней")
    def proceed_to_checkout(self) -> None:
        """
        Находит кнопку проверки корзины и кликает по ней
        """
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    @allure.step("Находим элементы формы и заполняем их")
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: int) -> None:
        """
        Находит элементы формы и заполняет их
        """
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_FIELD).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    @allure.step("Находим элемент 'Итоговая сумма' и выводим его значение")
    def get_total_price(self) -> str:
        """
        Находит элемент 'Итоговая сумма' и выводит его значение
        """
        return self.driver.find_element(*self.TOTAL_PRICE_LABEL).text

    @allure.step("Находим кнопку 'Завершить' и кликаем по ней")
    def finish_checkout(self) -> None:
        """
        Находит кнопку 'Завершить' и кликает по ней
        """
        self.driver.find_element(*self.FINISH_BUTTON).click()

    @allure.step("Находим кнопку возврата в каталог товаров и кликаем по ней")
    def go_back_to_products(self) -> None:
        """
        Находит кнопку возврата в каталог товаров и кликает по ней
        """
        self.driver.find_element(*self.BACK_TO_PRODUCTS_BUTTON).click()