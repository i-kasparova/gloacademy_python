# Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
# Для каждого введенного числа проверить:
# если число меньше 10, то пропускаем это число
# если число больше 100, то прекращаем считывать числа
# в остальных случаях вывести это число обратно на консоль в отдельной строке.
# Примечание: гарантируется, что число больше 100 точно встречается!

while True:
    n = int(input())
    if n < 10:
        continue
    if n > 100:
        break
    print(n)