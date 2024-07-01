from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#Запускаем браузер
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://uitestingplayground.com/classattr")

# Находим и кликаем на синюю кнопку
blue_button = driver.find_element(by=By.CLASS_NAME, value="btn-primary")

blue_button.click()
sleep(1)

print("Blue button clicked")

# Закрываем браузер
driver.quit()

# Запустил скрипт 3 раза подряд. Работает одинаково.