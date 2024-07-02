from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#Запускаем браузер
driver = webdriver.Firefox()

# Открываем страницу в Firefox
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Кликаем на кнопку "Add Element" пять раз
for _ in range(5):
    driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]').click()
    sleep(1)  # Ждем некоторое время после каждого клика

# Собираем список кнопок "Delete"
delete_buttons = driver.find_elements(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')

# Выводим размер списка
print("Размер списка кнопок Delete:", len(delete_buttons))

# Закрываем браузер
driver.quit()