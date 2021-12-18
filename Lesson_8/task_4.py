# Дано натуральное число n (n ≥ 10). Напишите программу, которая определяет его максимальную и минимальную цифры.

n = int(input())
max = 0
min = n % 10

while n != 0:
    last_digit = n % 10
    if last_digit > max:
        max = last_digit
    if last_digit < min:
        min = last_digit
    n = n // 10

print('Максимальная цифра равна', max)
print('Минимальная цифра равна', min)
