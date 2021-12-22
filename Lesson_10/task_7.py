# По данным ФИО сформируйте строку, содержащую фамилию с инициалами.

last_name = input()
name = input()
surname = input()

print(last_name, ' ', name[:1], '.', surname[:1], '.', sep = '')
