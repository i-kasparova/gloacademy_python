# Задание 7
# Дано натуральное число, не превосходящее 1 000 000 000. Найдите сумму последних трех цифр. Последние цифры – это те, которые справа в числе.

# Пример:
# Ввод:
# 14263584
# Вывод должен следующим:
# У числа 14263584 сумма последних трех цифр равна 17

from math import fmod

n = int(input())
print('У числа', n, 'сумма последних трех цифр равна', int(fmod(n, 1000)) // 100 + int(fmod(n, 100)) // 10 + int(fmod(n, 10)))