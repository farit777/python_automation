#from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открываем страницу
driver.get("http://uitestingplayground.com/textinput")

# Создаем объект waiter
waiter = WebDriverWait(driver, 30)

input_text = 'SkyPro'

# Вводим текст в поле
driver.find_element(by=By.CSS_SELECTOR, value='#newButtonName').send_keys(input_text)

# Кликаем по синей кнопке
driver.find_element(by=By.CSS_SELECTOR, value='#updatingButton').click()

# Ожидаем появление нового имени на кнопке
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#updatingButton'), input_text))

# Выводим текст кнопки в консоль
print(driver.find_element(by=By.CSS_SELECTOR, value='#updatingButton').text)

# Закрываем окно
driver.quit()