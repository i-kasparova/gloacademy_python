# Задание 6
# Вводится одно целое четырехзначное число. Выведите максимальную цифру числа.
#
# Пример:
# Ввод:
# 9 045
# Вывод должен следующим:
# У числа 9045 максимальная цифра равна 9

from math import fmod

n = int(input())

thous = n // 1000
hundr = int(fmod(n, 1000)) // 100
dec = int(fmod(n, 100)) // 10
unit = int(fmod(n, 10))

print('У числа', n, 'максимальная цифра равна', max(thous, hundr, dec, unit))