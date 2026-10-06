from selenium import webdriver


def test_session_storage_auth():
    # Ваши токены сессий, скопированные из браузера
    token_1 = "N2IwNDI2MmQtMDBlNy00M2E1LWJkZjQtYzA5ZjJkZjljODkz"
    token_2 = "ZWVjYjc3YWYtZmI1MC00M2NhLWE3ODgtMzk4OGUyMjBiZTcy"

    # Формируем куки для пользователей
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
        # 1. Откройте главную страницу сайта
        driver.get("https://gitflic.ru")

        # 2. Установите cookie пользователя 1
        driver.add_cookie(cookie_user_1)

        # 3. Обновите страницу
        driver.refresh()

        # 4. Перейдите на страницу пользователя 1
        # Используем короткий относительный путь, чтобы избежать опечаток
        driver.get(driver.current_url + "user/lana_skypro")

        # 5. Сохраните текущий URL
        url_user_1 = driver.current_url

        # 6. Разлогиньтесь (очистите куки)
        driver.delete_all_cookies()

        # 7. Установите cookie пользователя 2
        driver.get("https://gitflic.ru")
        driver.add_cookie(cookie_user_2)

        # 8. Обновите страницу
        driver.refresh()

        # 9. Перейдите на страницу пользователя 2
        driver.get(driver.current_url + "user/veta_skypro")

        # 10. Сохраните текущий URL
        url_user_2 = driver.current_url

        # 11. Проверьте, что URL для пользователей различаются
        msg = f"URL совпали ({url_user_1}), авторизация не сработала!"
        assert url_user_1 != url_user_2, msg

    finally:
        driver.quit()
