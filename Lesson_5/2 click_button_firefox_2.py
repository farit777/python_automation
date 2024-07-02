from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#Запускаем браузер
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Находим и кликаем на синюю кнопку с плавающим ID
blue_button = driver.find_element(by=By.CSS_SELECTOR, value="button.btn-primary")

for i in range(1,4):
    blue_button.click()
    print(f'Кнопка нажата {i} раз(а)')
    
sleep(1)

print('Button clicked')

sleep(1)

# Закрываем браузер
driver.quit()