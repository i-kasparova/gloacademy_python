# Угадай число

from random import randint


def is_valid_user(user_input, max):
    if user_input.isdigit():
        user_number = int(user_input)
        if user_number >= 1 and user_number <= max:
            return True
        else:
            return False
    else:
        return False


def is_valid_max(max):
    if max.isdigit():
        return True
    else:
        return False


def is_valid_again(yesno):
    if yesno.isdigit():
        user_answer = int(yesno)
        if user_answer == 1 or user_answer == 2:
            return True
        else:
            return False
    else:
        return False

print('Добро пожаловать!')

while True:

    while True:
        print('До какого числа загадывать?')
        max = input()
        if is_valid_max(max):
            max = int(max)
            break

    secret_number = randint(1, int(max))
    attempts = 0

    while True:
        user_input = input(f'Введите число от 1 до {max}: ')

        if not is_valid_user(user_input, max):
            continue

        user_number = int(user_input)

        if secret_number > user_number:
            print('Загаданное число больше, чем введенное вами число')
            attempts += 1
        elif secret_number < user_number:
            print('Загаданное число меньше, чем введенное вами число')
            attempts += 1
        else:
            print('УРА! Вы угадали загаднное число!')
            attempts += 1
            print(f'Количество попыток: {attempts}')
            break

    while True:
        print('Сыграем еще? 1 -- Да, 2 -- Нет')
        onceagain = (input())

        if not is_valid_again(onceagain):
            continue

        yesno = int(onceagain)
        print(yesno)
        if yesno == 1:
            willwecontinue = 1
            break
        else:
            willwecontinue = 0
            break
    
    if not willwecontinue:
        break
    
# Оптимальным алгоритмом является бинарный поиск, т.е. деление пополам, поэтому начинать следует с середины
# В случае с поиском 22 из 100:
# попытка 1: 50
# попытка 2: 25
# попытка 3: 12
# попытка 4: 18
# попытка 5: 22
#
# итого 5 попыток
