from selenium import webdriver
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


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._checkout_btn = (By.ID, "checkout")

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self._checkout_btn))
        self.driver.find_element(*self._checkout_btn).click()


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


def test_saucedemo_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        login_page = LoginPage(driver)
        shop_page = MainShopPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        shop_page.add_product_to_cart("sauce-labs-backpack")
        shop_page.add_product_to_cart("sauce-labs-bolt-t-shirt")
        shop_page.add_product_to_cart("sauce-labs-onesie")

        shop_page.go_to_cart()
        cart_page.click_checkout()

        checkout_page.fill_checkout_form("Иван", "Иванов", "123456")
        checkout_page.click_continue()

        total_text = checkout_page.get_total_price()

        assert total_text == "Total: $58.29", (
            f"Ожидалась сумма Total: $58.29, но получена {total_text}"
        )

    finally:
        driver.quit()
