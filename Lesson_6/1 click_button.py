#from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открываем страницу
driver.get("http://uitestingplayground.com/ajax")

# Создаем объект waiter
waiter = WebDriverWait(driver, 30)

# Кликаем по кнопке
driver.find_element(by=By.CSS_SELECTOR, value='button.btn-primary').click()

# Ожидаем появление плашки
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#content > p:nth-child(1)'), "Data loaded with AJAX get request."))

# Выводим тект плашки в консоль
print(driver.find_element(by=By.CSS_SELECTOR, value='#content > p:nth-child(1)').text)

# Закрываем окно
driver.quit()