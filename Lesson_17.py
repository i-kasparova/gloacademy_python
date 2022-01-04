from random import randint

def generate_secret_word():
    digits = [0,1,2,3,4,5,6,7,8,9]
    secret_word = ''

    for i in range(4):
        random_index = randint(0, len(digits)-1)
        secret_word += str(digits[random_index])
        digits.pop(random_index)
    
    return secret_word

def is_valid_user_word(user_word, secret_word):
    list = []
    user_word_int = int(user_word)

    if not user_word.isdigit() or len(user_word) != len(secret_word):
        return False
    
    for i in range(len(user_word)):
        if user_word[i].count != 1:
            return False

    return True
 
def calculate_bulls_count(user_word, secret_word):
    counter = 0
    for i in range(len(secret_word)):
        if secret_word[i] == user_word[i]:
            counter += 1

    return counter

def calculate_cows_count(user_word, secret_word):
    counter = 0
    for i in range(len(secret_word)):
        if secret_word[i] != user_word[i] and user_word[i] in secret_word:
            counter += 1
    
    return counter

def is_valid_again(answer):
    if answer == 'да' or answer == 'нет':
        return True
    else:
        return False

print('Найди число, задуманное компьютером!')

while True:
    secret_word = generate_secret_word()
    while True:

        while True:
            user_word = input()
            if not is_valid_user_word(user_word, secret_word):
                print('Ошибка ввода.')
                continue
            else:
                break

        bulls_count = calculate_bulls_count(user_word, secret_word)
        cows_count = calculate_cows_count(user_word, secret_word)

        print(f'{bulls_count} быков, {cows_count} коров')

        if bulls_count == 4:
            print('Ура! Ты победил!')
            break
    
    while True:
        print('Хотите сыграть еще? (Да/Нет)')
        onceagain = input().lower()

        if not is_valid_again(onceagain):
            continue
        else:
            break

    if onceagain.lower() == 'да':
        print()
        continue
    else:
        break
