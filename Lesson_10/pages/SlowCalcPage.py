import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SlowCalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, 'input#delay')
        self.buttons = {
            "7": (By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)"),
            "+": (By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)"),
            "8": (By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)"),
            "=": (By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning"),
        }
        self.result_display = (By.CSS_SELECTOR, "div.screen")

    @allure.step("Находим елемент 'delay' и заполняем его")
    def set_delay(self, delay: str) -> None:
        """
        Находит елемент 'delay' и заполняет его
        """
        delay_input_element = self.driver.find_element(*self.delay_input)
        self.driver.execute_script("arguments[0].setAttribute('value', arguments[1])", delay_input_element, delay)

    @allure.step("Выбираем из списка значения ключей словаря находим одноименные кнопки и кликаем по ним")
    def click_button(self, button_key: list) -> None:
        """
        Выбирает из списка значения ключей словаря находит одноименные кнопки и кликает по ним
        """
        button = self.driver.find_element(*self.buttons[button_key])
        button.click()
    
    @allure.step("Ждем появления элемента 'Результат'")
    def wait_for_result(self, expected_result: str, timeout=20) -> None:
        """
        Ждет появления элемента 'Результат' и задает время ожидания
        """
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(self.result_display, expected_result))

    @allure.step("Находим элемент 'Результат' и возвращаем его значение")
    def get_result(self) -> str:
        """
        Находит элемент 'Результат' и возвращает его значение
        """
        return self.driver.find_element(*self.result_display).text