from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._username = (By.ID, "user-name")
        self._password = (By.ID, "password")
        self._login_btn = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://saucedemo.com")

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self._username))
        self.driver.find_element(*self._username).send_keys(username)
        self.driver.find_element(*self._password).send_keys(password)
        self.driver.find_element(*self._login_btn).click()
