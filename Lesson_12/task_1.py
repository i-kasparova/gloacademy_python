# Дано два натуральных числа. Найдите количество разрядов каждого из них и выведите их произведение.

def count_digits(number):
    total = 0
    while number > 0:
        total += 1
        number = number // 10
    return total

number1 = int(input())
number2 = int(input())
print(count_digits(number1) * count_digits(number2))
