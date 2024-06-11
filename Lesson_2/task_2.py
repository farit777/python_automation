# Функция определяет високосность года дает ответ True/False
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    

# Получение года от пользователя
year = int(input("Введите год в формате ГГГГ: "))

# Вывод ответа
print(f'год {year}: {is_year_leap(year)}')

