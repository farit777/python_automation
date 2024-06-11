import math

# Функция вычисления площади квадрата
def square(side):
    area = side ** 2
    return math.ceil(area)

# Получение от пользователя длины стороны квадрата
side = float(input("Введите длину стороны квадрата: "))

# Вывод площади квадрата
print(square(side))
