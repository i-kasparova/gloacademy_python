# Определите среднее арифметическое элементов последовательности, завершающейся числом 0.

n = int(input())
total = 0
k = 0

while n !=0:
    total = total + n
    k += 1
    n = int(input())

print(total / k)
