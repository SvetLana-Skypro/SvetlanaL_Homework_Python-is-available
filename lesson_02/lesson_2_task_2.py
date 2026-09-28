def is_year_leap(year):
    """Функция проверяет, является ли год високосным."""
    if year % 4 == 0:
        return True
    else:
        return False


check_year = 2029
result = is_year_leap(check_year)

print(f"год {check_year}: {result}")
