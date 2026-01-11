#Exercise 1
#Створимо функцію, яка зберігає стан даних
def caching_fibonacci():
    cache = {}
    #Створимо функцію, що обчислює числа Фібаночі
    def fibonacci(n):
        if n <= 0:
            return 0
        if n ==1:
            cache [n] = 1
            return 1
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
            return cache[n]
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
print(fib(1))
print(fib(-2))
print(fib(0))

#Exercise 2
import re
from typing import Callable

#Створимо генератор, який знаходить числа і повертає їх
def generator_numbers(text: str):
    numbers = re.findall(r"\d+\.\d+", text)
    for number in numbers:
        yield number

# Створимо функцію, яка використовує генератор для обчислення суми чисел у строці
def sum_profit(text: str, func: Callable):
    gen = func(text)
    sum_number = 0
    while True:
        try:
            number = next(gen)
            sum_number += float(number)
        except StopIteration:
            break
    return sum_number


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід," \
" доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")



