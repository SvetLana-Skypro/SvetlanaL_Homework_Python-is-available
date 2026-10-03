from selenium import webdriver

def test_session_storage_auth():
    token_1 = "N2IwNDI2MmQtMDBlNy00M2E1LWJkZjQtYzA5ZjJkZjljODkz"
    token_2 = "ZWVjYjc3YWYtZmI1MC00M2NhLWE3ODgtMzk4OGUyMjBiZTcy"

    cookie_user_1 = {
        "name": "SESSION",
        "value": token_1,
        "domain": ".gitflic.ru",
        "path": "/",
    }
    cookie_user_2 = {
        "name": "SESSION",
        "value": token_2,
        "domain": ".gitflic.ru",
        "path": "/",
    }

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://gitflic.ru")

        driver.add_cookie(cookie_user_1)

        driver.refresh()

        driver.get(driver.current_url + "user/lana_skypro")

        url_user_1 = driver.current_url

        driver.delete_all_cookies()

        driver.get("https://gitflic.ru")
        driver.add_cookie(cookie_user_2)

        driver.refresh()

        driver.get(driver.current_url + "user/veta_skypro")

        url_user_2 = driver.current_url

        msg = f"URL совпали ({url_user_1}), авторизация не сработала!"
        assert url_user_1 != url_user_2, msg

    finally:
        driver.quit()
