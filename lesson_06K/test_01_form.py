import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fill_form(driver):
    url = (
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )
    driver.get(url)

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait = WebDriverWait(driver, 10)

    zip_code_alert = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    zip_class = zip_code_alert.get_attribute("class")
    assert "alert-danger" in zip_class, (
        "Поле Zip code должно быть подсвечено красным!"
    )

    green_fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company",
    ]

    for field_id in green_fields:
        field_element = driver.find_element(By.ID, field_id)
        field_class = field_element.get_attribute("class")
        assert "alert-success" in field_class, (
            f"Поле {field_id} должно быть подсвечено зеленым!"
        )
