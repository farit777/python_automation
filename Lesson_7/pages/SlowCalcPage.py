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

    def set_delay(self, delay):
        delay_input_element = self.driver.find_element(*self.delay_input)
        self.driver.execute_script("arguments[0].setAttribute('value', arguments[1])", delay_input_element, delay)

    def click_button(self, button_key):
        button = self.driver.find_element(*self.buttons[button_key])
        button.click()
    
    def wait_for_result(self, expected_result, timeout=20):
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(self.result_display, expected_result))

    def get_result(self):
        return self.driver.find_element(*self.result_display).text