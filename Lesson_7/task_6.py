# На вход программе подается натуральное число n. Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно), которые оканчиваются на 1, 3 или 7.

n = int(input())
total = 0

for i in range (1, n+1):
    if (i % 10 == 1) or (i % 10 == 3) or (i % 10 == 7):
        total += i

print(total)