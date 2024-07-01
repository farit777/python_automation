from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#Запускаем браузер
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Находим поле для ввода и вводим текст "1000"
input_field = driver.find_element(by=By.TAG_NAME, value="input")
input_field.send_keys("1000")

# Ждем некоторое время
sleep(2)

# Очищаем поле
input_field.clear()
sleep(2)

# Вводим текст "999"
input_field.send_keys("999")
sleep(2)

# Закрываем браузер
driver.quit()