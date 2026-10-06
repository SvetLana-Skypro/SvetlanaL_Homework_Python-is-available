from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)
        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._screen = (By.CSS_SELECTOR, ".screen")

    def open(self):
        url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.driver.get(url)

    def set_delay(self, delay_value):
        delay_field = self.driver.find_element(*self._delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay_value))

    def click_button(self, button_text):
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()

    def wait_for_result(self, expected_result):
        self.wait.until(
            EC.text_to_be_present_in_element(self._screen, expected_result)
        )

    def get_result(self):
        return self.driver.find_element(*self._screen).text
