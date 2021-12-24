# Необходимо вычислить произведение двух максимальных элементов списков a и b.
# На первой строке вводятся элементы первого списка через пробел.
#На второй строке вводятся элементы второго списка через пробел.

def search_max(s):
    numbers = s.split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    return max(numbers)

line1 = input()
line2 = input()
print(search_max(line1) * search_max(line2))
