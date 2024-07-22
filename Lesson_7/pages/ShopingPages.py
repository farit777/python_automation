#import pytest
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

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

class ProductsPage(BasePage):
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TO_CART_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_TO_CART_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_BUTTON = (By.ID, "shopping_cart_container")

    def add_products_to_cart(self):
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

    def proceed_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_FIELD).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total_price(self):
        return self.driver.find_element(*self.TOTAL_PRICE_LABEL).text

    def finish_checkout(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def go_back_to_products(self):
        self.driver.find_element(*self.BACK_TO_PRODUCTS_BUTTON).click()