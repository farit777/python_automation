
lst1 = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
lst2 = []

for num in lst1:
    if num < 30 and num % 3 == 0:
        lst2.append(num)

# Лучше так:
# lst2 = [num for num in lst if num < 30 and num % 3 == 0]

print(lst2) # Выводит [15, 3, 21, 9]
