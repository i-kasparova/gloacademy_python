# Вводится натуральное число a. Определите является ли число простым.

a = int(input())
flag = 0

for i in range (1, a+1):
    if i != 1 and i != a:
        if a % i == 0:
            flag = 1
            print('NO')
            break

if flag == 0:
    print('YES')   
