from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self, product_id):
        locator = (By.ID, f"add-to-cart-{product_id}")
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def go_to_cart(self):
        self.driver.find_element(*self._cart_link).click()
