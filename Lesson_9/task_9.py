# Дано натуральное число n.
# Напишите программу, которая находит цифровой корень данного числа.

n = int(input())
d_root = 0

while n // 10 != 0:
    while n != 0:
        last_digit = n % 10
        d_root += last_digit
        n = n // 10
    n = d_root
    d_root = 0

print(n)
