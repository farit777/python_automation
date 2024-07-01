# Клик по кнопке с плавающим ID (по ID искать нельзя)
# Кнопка ищется по CSS селектору и классу кнопки, которые вряд ли изменятся
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открываем страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Находим и кликаем на синюю кнопку с плавающим ID
blue_button = driver.find_element(by=By.CSS_SELECTOR, value="button.btn-primary")
blue_button.click()

print('Button clicked')

sleep(1)

# Закрываем браузер
driver.quit()