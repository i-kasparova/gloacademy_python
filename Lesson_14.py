from random import randint

def ask_question(question):
    print(question, 'Введите "Да" или "Нет"')

    while True:
        answer = input().lower()
        if answer == 'да':
            return True
        elif answer == 'нет':
            return False
        else:
            print('Это не ответ! :(\n')
            print(question, 'Введите "Да" или "Нет"')
            continue
        break

def generate_password(length, chars):
    password = ''
    
    for i in range(length):
        random_index = randint(0, len(chars)-1)
        password += chars[random_index]
    
    return password


def is_valid_number(number):
    if number.isdigit():
        return True
    else:
        print('Это не число!\n')
        return False

print('Привет! Я генератор паролей.\nЯ задам пару уточняющих вопросов, на основе которых сгенерирую пароль\n')

while True:
    print('Сколько паролей хотите создать? ')
    number = input()
    if is_valid_number(number):
        number = int(number)
        break

for i in range (number):

    while True:
        print('Введите длину пароля:')
        length = input()
        if is_valid_number(length):
            length = int(length)
            break

    enabled_chars = ''

    digits = '0123456789'
    latin_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    latin_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cyrillic_lowercase = 'абвгдежзиклмнопрстуфхцчшщъыьэюя'
    cyrillic_uppercase = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    punctuation = '!#$%&*+=?@^_'

    while True:

        digits_enabled = ask_question('Включать ли цифры?')
        latin_lowercase_enabled = ask_question('Включать ли строчные латинские буквы?')
        latin_uppercase_enabled = ask_question('Включать ли заглавные латинские буквы?')
        cyrillic_lowercase_enabled = ask_question('Включать ли строчные русские буквы?')
        cyrillic_uppercase_enabled = ask_question('Включать ли заглавные русские буквы?')
        punctuation_enabled = ask_question('Включать ли знаки пунктуации?')

        if digits_enabled :
            enabled_chars += digits

        if latin_lowercase_enabled:
            enabled_chars += latin_lowercase

        if latin_uppercase_enabled:
            enabled_chars += latin_uppercase

        if cyrillic_lowercase_enabled:
            enabled_chars += cyrillic_lowercase

        if cyrillic_uppercase_enabled:
            enabled_chars += cyrillic_uppercase

        if punctuation_enabled:
            enabled_chars += punctuation
        
        if enabled_chars == '':
            print('Мне не из чего генерировать пароль :( Попробуем еще раз!\n')
            continue
        else:
            break
    
    while True:
        password = generate_password(length, enabled_chars)

        print(f'{password}\n')

        anotherone = ask_question('Понравился пароль? Если вы введете "Нет", я сгенерирую новый.')
        if not anotherone:
            continue
        else:
            print(f'Это {i+1}-й из {number} паролей :)\n')
            break
