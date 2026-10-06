from selenium import webdriver
from pages.calculator_page import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        calc_page = CalculatorPage(driver)

        calc_page.open()
        calc_page.set_delay(45)

        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

        calc_page.wait_for_result("15")
        final_result = calc_page.get_result()

        assert final_result == "15", (
            f"Ожидался результат 15, но получен {final_result}"
        )

    finally:
        driver.quit()
