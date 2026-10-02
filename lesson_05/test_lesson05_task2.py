from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    name_input = driver.find_element(By.NAME, "custname")
    name_input.send_keys("Светлана")

    submit_button = driver.find_element(By.XPATH, "//form//button")
    submit_button.click()

    driver.implicitly_wait(2)

    assert driver.current_url != (
        "https://qa-territory.online"
    ), f"URL не изменился: {driver.current_url}"

    driver.quit()
