
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#Запускаем браузер
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(3)

# Находим и кликаем на кнопку "Close" в модальном окне
close_button = driver.find_element(by=By.XPATH, value="//p[text()='Close']")

close_button.click()

print('Button clicked')

# Закрываем браузер
driver.quit()