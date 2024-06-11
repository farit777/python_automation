def bank(X, Y):
    total = X
    for _ in range(Y):
        total += total * 0.10
    return total

# Пример использования: начальная сумма 1000, итог через 5 лет
X = 1000
Y = 7
print(bank(X, Y))
