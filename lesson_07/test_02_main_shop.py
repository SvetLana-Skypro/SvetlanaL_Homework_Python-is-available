from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_shop_page import MainShopPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


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
