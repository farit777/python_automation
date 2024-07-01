from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#Запускаем браузер
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/login")

# Находим поле для ввода username и вводим значение "tomsmith"
username_field = driver.find_element(by=By.NAME, value="username")
username_field.send_keys("tomsmith")

# Находим поле для ввода password и вводим значение "SuperSecretPassword!"
password_field = driver.find_element(by=By.NAME, value="password")
password_field.send_keys("SuperSecretPassword!")

sleep(2)

# Находим и кликаем на кнопку "Login"
login_button = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")
login_button.click()

# Закрываем браузер
driver.quit()