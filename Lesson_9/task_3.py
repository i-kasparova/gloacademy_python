# Вводится натуральное число a. Определите содержит ли введенное число, цифру 1.

# Вводится натуральное число a. Определите содержит ли введенное число, цифру 1.

a = int(input())
flag = 0

while a != 0:
    if a % 10 == 1:
        flag = 1
        break
    a = a // 10

if flag == 1:
    print('YES')
else:
    print('NO')
