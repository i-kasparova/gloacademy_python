# Даны две строчные буквы латинского алфавита.
# Выведите на одной строке через пробел все строчные буквы латинского алфавита в алфавитном порядке, которые находятся между данными символами, а также их самих.

c1 = input()
c2 = input()

if ord(c1) < ord(c2):
    for i in range (ord(c1), ord(c2)+1):
        print(chr(i), end = ' ')
else:
    for i in range(ord(c2), ord(c1)+1):
        print(chr(i), end=' ')
