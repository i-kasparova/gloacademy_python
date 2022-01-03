def generate_user_word(word):
    return '*' * len(word)

def update_user_word(secret_word, user_word, char):
    new_user_word = ''
    for i in range(len(secret_word)):
        if secret_word[i] == char:
            new_user_word += char
        else:
            new_user_word += user_word[i]
    
    return new_user_word

def was_before(char, was_list):
    if char in was_list:
        return True
    else:
        was_list.append(char)
        return False

def is_valid_char(char):
    flag = 0
    for i in range(len(cyrillic_lowercase)):
        if cyrillic_lowercase[i] == char:
            flag = 1
        
    if flag:
        return True
    else:
        return False

def is_valid_again(answer):
    if answer == 'да' or answer == 'нет':
        return True
    else:
        return False

cyrillic_lowercase = 'абвгдежзиклмнопрстуфхцчшщъыьэюя'
print('Вопрос: Название нек-рых высших учебных заведений')
secret_word = 'академия'
user_word = generate_user_word(secret_word)
print(user_word)
try_number = 0
was_list = []

while True:
    while user_word != secret_word:

        while True:
            print('Введите букву:')
            user_char = input().lower()

            if len(user_char) != 1:
                continue

            if was_before(user_char, was_list):
                print('Такая буква уже была. Введите другую.')
                continue

            if is_valid_char(user_char):
                try_number += 1
                break

        new_user_word = update_user_word(secret_word, user_word, user_char)

        if user_word == new_user_word:
            print('К сожалению, такой буквы в слове нет')
        else:
            print('Есть такая буква!')
            user_word = new_user_word
        
        print(user_word)

    print(f'Ура! Вы угадали слово c {try_number}-й попытки и выиграли ааавтомобиииль!')

    while True:
        print('Хотите сыграть еще? ("Да" или "Нет")')
        onceagain = input().lower()

        if not is_valid_again(onceagain):
            continue
        else:
            break
    
    if onceagain.lower() == 'да':
        user_word = generate_user_word(secret_word)
        continue
    else:
        break
