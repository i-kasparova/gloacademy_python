# Вводится строка, содержащая натуральные числа, отделенные символом пробела.
# Напишите программу, которая подсчитывает, сколько пар элементов, равных друг другу.

s = input()
list = s.split()
total = 0

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] == list[j]:
            total += 1
            list.pop(j)

print(total)
