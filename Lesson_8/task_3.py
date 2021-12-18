# Вводится натуральное число a. Определите является ли данное число замечательным.

a = int(input())
copy = a
total = 0

while copy != 0:
    total += copy % 10
    copy = copy // 10

if a % total == 0:
    print('YES')
else:
    print ('NO')
