# Функция
def fizz_buzz(n):
    '''
    Функция печатает числа от 1 до n. При этом:
    если число делится на 3, печатает Fizz;
    если число делится на 5, печатает Buzz;
    если число делится на 3 и на 5, печатает FizzBuzz
    '''
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Получение числа от пользователя
n = int(input("Введите число: "))

# Вызов функции
fizz_buzz(n)
