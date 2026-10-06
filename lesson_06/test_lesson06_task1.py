from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    driver.maximize_window()

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        finish_text_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )

        driver.save_screenshot("dynamic_loading_success.png")

        actual_text = finish_text_element.text
        msg = "Ожидался 'Hello World!', но получен '{actual_text}'"
        assert actual_text == "Hello World!", msg

    finally:
        driver.quit()
