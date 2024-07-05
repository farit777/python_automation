from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открываем страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Создаем объект waiter
waiter = WebDriverWait(driver, 40)

# Ожидаем закгрузки всех картинок
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#text'), 'Done'))

# Получение и вывод атрибута "src" у третьей картинки с ID = "award"
award_image = driver.find_element(By.ID, "award")
src_attribute = award_image.get_attribute("src")
print(f"Атрибут 'src' у третьей картинки с ID = 'award': {src_attribute}")

# Закрываем окно
driver.quit()