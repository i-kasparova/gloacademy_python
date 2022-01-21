from random import randint

def is_numeric(user_answer):
    if user_answer.isdigit():
        return True

def is_correct(user_answer, i):
    global answers
    right_answer = answers[i]
    if user_answer == right_answer:
        return True
    else:
        return False

def result(count):
    if count == 0:
        return 'идиот'
    if count == 1:
        return 'кретин'
    if count == 2:
        return 'дурак'
    if count == 3:
        return 'нормальный'
    if count == 4:
        return 'талант'
    else:
        return 'гений'

def is_valid_again(answer):
    if answer == 'да' or answer == 'нет':
        return True
    else:
        return False

questions = [
    'Сколько будет два плюс два умножить на два?',
    'Бревно нужно распилить на 10 частей, сколько надо сделать распилов?',
    'Нв двух руках 10 пальцев. Сколько пальцев на пяти руках?',
    'Укол делают каждые полчаса. Сколько нужно минут для трех уколов?',
    'Пять свечей горело, две потухли. Сколько свечей осталось?'
]

answers = [6, 9, 25, 60, 2]

name = input('Добрый день! Как вас зовут?\n')

while True:
    count_right_answers = 0
    used_questions = []

    for i in range(len(questions)):

        while True:
            index = randint(0, len(questions)-1)
            if not index in used_questions and len(used_questions) != len(questions):
                used_questions.append(index)
                break

        print(f'Вопрос №{i+1}: {questions[index]}')
        
        while True:
            user_answer = input()
            if is_numeric(user_answer):
                user_answer = int(user_answer)
                if is_correct(user_answer, index):
                    count_right_answers += 1
                break
            else:
                print('Ошибка ввода.')
                continue
        
    print(f'Количество правильных ответов: {count_right_answers}. Вы {result(count_right_answers)}, {name}.\n')
    
    while True:
        print('Хотите пройти тест снова? (Да/Нет)')
        onceagain = input().lower()
        print()

        if is_valid_again(onceagain):
            break

    if not onceagain.lower() == 'да':
        break
