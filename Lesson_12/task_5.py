# Напишите функцию, которая принимает в качестве аргумента строковое представление корректной даты и возвращает значение True, если дата является звездной
# и False в противном случае.

def count_star_date(date):
    numbers = date.split('.')

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    
    if numbers[0] * numbers[1] == numbers[2] % 100:
        return True
    else:
        return False

date = input()
print(count_star_date(date))
