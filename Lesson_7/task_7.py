# На вход программе подается натуральное число n. Напишите программу, которая подсчитывает произведение тех чисел от 1 до n (включительно), которые оканчиваются на 2 или на 9.
# Если таких чисел нет в указанном диапазоне, то следует вывести 0.

n = int(input())
total = 1

for i in range (1, n+1):
    if (i % 10 == 2) or (i % 10 == 9):
        total *= i

if total == 1:
    print('0')
else:
    print(total)
