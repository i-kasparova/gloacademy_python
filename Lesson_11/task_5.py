# Дан список. Выведите те элементы, которые встречаются в списке только один раз.

numbers = input().split()

for i in numbers:
    if numbers.count(i) == 1:
        print(i, end = ' ')
