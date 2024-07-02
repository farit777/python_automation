from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открываем страницу
driver.get("http://uitestingplayground.com/classattr")

# Находим и кликаем на синюю кнопку 3 раза
blue_button = driver.find_element(by=By.CLASS_NAME, value="btn-primary")
for i in range(1,4):
    blue_button.click()
    sleep(1)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    print(f"Синяя конпка нажата {i} раз(а)")
    sleep(1)

# Закрываем браузер
driver.quit()

# Запустил скрипт 3 раза подряд. Работает одинаково.