def month_to_season(month):
    '''
    принимает один аргумент — номер месяца
    возвращает название сезона, к которому относится этот месяц.
    Например, передаем 2, на выходе получаем «Зима».
    '''
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Введите число от 1 до 12"

# Получения месяца от пользователя
n = int(input("Введите число от 1 до 12: "))

# вывод результата
print(month_to_season(n))
