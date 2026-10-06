from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._first_name = (By.ID, "first-name")
        self._last_name = (By.ID, "last-name")
        self._postal_code = (By.ID, "postal-code")
        self._continue_btn = (By.ID, "continue")
        self._total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.wait.until(EC.visibility_of_element_located(self._first_name))
        self.driver.find_element(*self._first_name).send_keys(first_name)
        self.driver.find_element(*self._last_name).send_keys(last_name)
        self.driver.find_element(*self._postal_code).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self._continue_btn).click()

    def get_total_price(self):
        self.wait.until(EC.visibility_of_element_located(self._total_label))
        return self.driver.find_element(*self._total_label).text
