from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru/") #браузер откроет страницу
driver.get("https://vk.com/") #перейдет на следующую страницу
driver.set_window_size(640, 460) #окно браузера уменьшится под параметры
sleep(10)