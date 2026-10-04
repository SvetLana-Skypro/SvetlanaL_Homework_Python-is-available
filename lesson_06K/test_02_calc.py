from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    try:
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()

        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        wait = WebDriverWait(driver, 50)

        result_locator = (By.CSS_SELECTOR, ".screen")
        wait.until(EC.text_to_be_present_in_element(result_locator, "15"))

        final_result = driver.find_element(*result_locator).text
        assert final_result == "15", (
            f"Ожидался результат 15, но получен {final_result}"
        )

    finally:
        driver.quit()
