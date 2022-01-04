def create_field():
    field = []
    for i in range(3):
        field.append(['*'] * 3)
    
    return field

def print_field(field):
    for i in range(3):
        for j in range(3):
            print(field[i][j], end = ' ')
        print()

def is_correct_index(index):
    if not index.isdigit():
        return False
    else:
        index = int(index)
        if index >= 1 and index <= 3:
            return True
        else:
            return False

def is_busy(row, column):
    if field[row-1][column-1] != '*':
        return True
    else:
        False

def win(field):
    for i in range(3):
        if field[i][0] != '*' and field[i][0] == field[i][1] == field[i][2]:
            return True
    
    for j in range(3):
        if field[0][j] != '*' and field[0][j] == field[1][j] == field[2][j]:
            return True
    
    if field[0][0] != '*' and field[0][0] == field[1][1] == field[2][2]:
        return True
    
    if field[2][0] != '*' and field[2][0] == field[1][1] == field[2][2]:
        return True
    
    return False

def end_game(field):

    if win(field):
        return True

    for i in range(3):
        for j in range(3):
            if field[i][j] == '*':
                return False

    return True

def is_valid_again(answer):
    if answer == 'да' or answer == 'нет':
        return True
    else:
        return False

field = create_field()
current_symbol = 'X'

while True:
    while not end_game(field):
        print_field(field)

        while True:
            while True:
                row = input('Введите номер строки: ')
                if not is_correct_index(row):
                    print('Ошибка ввода.')
                    continue
                else:
                    row = int(row)
                    break

            while True:
                column = input('Введите номер столбца: ')

                if not is_correct_index(column):
                    print('Ошибка ввода.')
                    continue
                else:
                    column = int(column)
                    break
            
            if is_busy(row, column):
                print('Это поле уже занято. Введите другие координаты.')
                continue
            else:
                field[row-1][column-1] = current_symbol
                break

        if current_symbol == 'X':
            current_symbol = '0'
        else:
            current_symbol = 'X'

    print_field(field)
    if current_symbol == 'X':
        print('Ура! Победил 0')
    else:
        print('Ура! Победил X')
    
    while True:
        print('Хотите сыграть еще? (Да/Нет)')
        onceagain = input().lower()

        if not is_valid_again(onceagain):
            continue
        else:
            break
    
    if onceagain.lower() == 'да':
        print()
        field = create_field()
        continue
    else:
        break
