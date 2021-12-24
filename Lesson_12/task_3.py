# Напишите функцию, которая принимает номер месяца и возвращает количество дней в данном месяце. Передаваемый аргумент находится в диапазоне от 1 до 12.

def count_days(month):
    thirty = [1, 4, 6, 7, 8, 11]
    thirty_one = [3, 5, 7, 9, 12]

    if month > 12:
        return 'Такого месяца не существует'
      
    if month in thirty:
        return 30
    elif month in thirty_one:
        return 31
    else:
        return 28
 
month = int(input())
print(count_days(month))
  
