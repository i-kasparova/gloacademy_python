# На вход программе подается натуральное число n, а затем n строк. Это наш банк слов, которые будет искать пользователь.
# Затем вводится еще одна строка — поисковый запрос пользователя.
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.

n = int(input())
list = []

for i in range(n):
    list.append(input())

query = input().lower()

for i in list:
    if i.lower().count(query):
        print(i)