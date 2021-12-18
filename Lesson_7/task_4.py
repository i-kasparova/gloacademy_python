# Даны два целых числа a и b. Напишите программу, которая выводит все ЧЕТНЫЕ числа на данном промежутке в возрастающем порядке, включая a и b.

a = int(input())
b = int(input())

if a == b:
    if a % 2 == 0:
        print(a)
elif a < b:
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)
else:
    for i in range(b, a + 1):
        if i % 2 == 0:
            print(i)
