# Последовательность состоит из целых чисел и завершается числом 0.
# Выведите произведение количества положительных и отрицательных чисел последовательности.

n = int(input())
positive = 0
negative = 0

while n !=0:
    if n > 0:
        positive += 1
    if n < 0:
        negative +=1
    n = int(input())

print(positive * negative)
