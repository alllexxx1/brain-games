import prompt
from random import randint


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def initialize_game():
    number = randint(0, 100)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (number, correct_answer)


def play_brain_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rules)
    right_answers = 3
    while right_answers:
        question, correct_answer = initialize_game()
        print(f'Question: {question}')
        user_answer = prompt.string('You answer: ')
        if user_answer != correct_answer:
            print(f''''{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!''')
            break
        else:
            print('Correct!')
            right_answers -= 1
    else:
         print(f'Congratulations, {name}!')
