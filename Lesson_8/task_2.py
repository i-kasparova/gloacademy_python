# Вводится натуральное число a. Найдите количество цифр 5 среди всех цифр числа a.

a = int(input())
total = 0

while a != 0:
    last_digit = a % 10
    if last_digit == 5:
        total += 1
    a = a // 10

print(total)
