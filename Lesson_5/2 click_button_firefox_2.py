from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#Запускаем браузер
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Находим и кликаем на синюю кнопку с плавающим ID
blue_button = driver.find_element(by=By.CSS_SELECTOR, value="button.btn-primary")
blue_button.click()

print('Button clicked')

sleep(1)

# Закрываем браузер
driver.quit()