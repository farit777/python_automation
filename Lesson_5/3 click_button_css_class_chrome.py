from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

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