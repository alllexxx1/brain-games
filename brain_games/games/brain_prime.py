from random import randint


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def initialize_game():
    number = randint(0, 100)
    if number % 2 == 0 or number <= 1:
        correct_answer = 'no'
    elif number == 2:
        correct_answer = 'yes'
    else:
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                correct_answer = 'no'
        correct_answer = 'yes'
    return (number, correct_answer)
