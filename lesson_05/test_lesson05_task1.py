from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    base_url = "https://httpbin.qa-territory.online/"
    driver.get(base_url)

    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_link.click()

    assert driver.current_url.endswith("/forms/post"), (
        "Ожидался URL, заканчивающийся на /forms/post, "
        f"но получили {driver.current_url}"
    )

    driver.back()

    assert driver.current_url == base_url, (
        f"Ожидался возврат на {base_url}, но получили {driver.current_url}"
    )

    driver.quit()
