def month_to_season(month_number):
    if month_number == 12 or month_number == 1 or month_number == 2:
        return "Зима"
    elif month_number == 3 or month_number == 4 or month_number == 5:
        return "Весна"
    elif month_number == 6 or month_number == 7 or month_number == 8:
        return "Лето"
    elif month_number == 9 or month_number == 10 or month_number == 11:
        return "Осень"
    else:
        return "Неверный номер месяца"


month = 2
season = month_to_season(month)

print(f"Месяц {month} — это {season}")
