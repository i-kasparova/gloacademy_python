# Вводится натуральное число a. Определите является ли число простым.
# Число называется простым, если у него только 2 делителя: 1 и само число.

a = int(input())
flag = 0

for i in range (1, a+1):
    if i != 1 and i != a:
        if a % i == 0:
            flag = 1

if flag == 0:
    print('YES')
else:
    print('NO')
