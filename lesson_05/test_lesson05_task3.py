from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    links = driver.find_elements(By.TAG_NAME, "a")

    assert len(links) == 9, f"Ожидалось 9 ссылок, но найдено {len(links)}"

    for link in links:
        assert link.is_displayed(), (
            f"Ссылка с текстом '{link.text}' не отображается"
        )

    first_link_text = links[0].text
    assert "1" in first_link_text, (
        f"Текст первой ссылки не содержит '1', получили: "
        f"'{first_link_text}'"
    )

    driver.quit()
