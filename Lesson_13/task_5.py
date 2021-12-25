# 1. Ввести верхнюю границу и присвоить ее max, min = 0
# 2. Вести (загадать) число в этом диапазоне
# 3. Вычислить следующее число по формуле min + (max - min) // 2
# 4. Сравнить полученное число с загаданным и получить ответ, больше или меньше загаданное число
# 5. Если загаданное число меньше, то присваивает результату формулы max, иначе -- min
# 6. Повторять шаги 3-5 до получения верного результата

def is_valid_secret_number(user_input, max):
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

while True:
    min = 0

    while True:
        print('До какого числа вы загадываете?')
        max = input()
        if is_valid_max(max):
            max = int(max)
            break
        
    while True:
        user_input = input(f'Загадайте число от 0 до {max}: ')
        if is_valid_secret_number(user_input, max):
            secret_number = int(user_input)
            break
    

    while True:
        if not max-min == 1:
            guess = min + (max - min) // 2
        else:
            guess = max

        print(f'Это {guess}? (1 -- больше, 2 -- меньше, 3 -- равно)')
        yesno = (int(input()))

        if yesno == 1:
            min = guess
        elif yesno == 2:
            max = guess
        else:
            print('УРА! Я угадал!')
            break
    
    while True:
        print('Сыграем еще? 1 -- Да, 2 -- Нет')
        onceagain = (input())

        if not is_valid_again(onceagain):
            continue

        yesno = int(onceagain)
        if yesno == 1:
            willwecontinue = 1
            break
        else:
            willwecontinue = 0
            break

    if not willwecontinue:
        print('Ну ты это, заходи если что :)')
        break
