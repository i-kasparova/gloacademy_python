# Дан текст, составленный из букв латинского алфавита и цифр. Напечатать все имеющиеся в нем цифры.

s = input()

for i in range(len(s)):
    if s[i].isdigit():
        print(s[i], end = '')
