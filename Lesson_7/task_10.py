# На вход программе подается натуральное число n, которое является количеством чисел в последовательности, которую пользователь должен будет ввести.
# Выведите YES, если все введенные числа нечетные. В противном случае выведите NO.

n = int(input())
flag = 1

for i in range (n):
    k = int(input())
    if k % 2 == 0:
        flag = 0

if flag == 1:
    print('YES')
else:
    print('NO')
