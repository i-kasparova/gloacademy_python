from random import randint
from pathlib import Path

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

def result(count, quantity):
    rate = count/quantity
    if rate == 0:
        return 'идиот'
    if rate > 0 and rate <= 0.2:
        return 'кретин'
    if rate > 0.2 and rate <= 0.4:
        return 'дурак'
    if rate > 0.4 and rate <= 0.6:
        return 'нормальный'
    if rate > 0.6 and rate <= 0.8:
        return 'талант'
    else:
        return 'гений'

def save_result(name, count, score):
    global path
    f = open(path, 'a')
    f.write(f'{name}|{count}|{score}\n')
    f.close()

def is_valid_yesno(answer):
    if answer == 'да' or answer == 'нет':
        return True
    else:
        return False

questions = [
    'Сколько будет два плюс два умножить на два?',
    'Бревно нужно распилить на 10 частей, сколько надо сделать распилов?',
    'На двух руках 10 пальцев. Сколько пальцев на пяти руках?',
    'Укол делают каждые полчаса. Сколько нужно минут для трех уколов?',
    'Пять свечей горело, две потухли. Сколько свечей осталось?'
]

answers = [6, 9, 25, 60, 2]
path = Path(Path.cwd(), 'Glo Academy', 'My_Tester', 'results.txt')

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
                print('Пожалуйста, введите число!')
                continue
    
    score = result(count_right_answers, len(questions))
    print(f'Количество правильных ответов: {count_right_answers}. Вы {score}, {name}.\n')
    
    save_result(name, count_right_answers, score)
    
    while True:
        print('Хотите пройти тест снова? (Да/Нет)')
        answer = input().lower()
        print()

        if is_valid_yesno(answer):
            break
    
    if not answer.lower() == 'да':
        while True:
            print('Хотите посмотреть результаты? (Да/Нет)')
            answer = input().lower()
            print()

            if is_valid_yesno(answer):
                break
        if not answer.lower() == 'да':
            break
        else:
            print(f"{'Имя':30}{'Кол-во правильных ответов':30}{'Результат':30}")
            f = open(path, 'r')
            for line in f:
                list = line.split('|')
                for e in list:
                    print(f'{e:30}', end='')
                print()
            break
