from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 0
MAX_NUM = 100


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def create_game_data():
    number = randint(MIN_NUM, MAX_NUM)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (number, correct_answer)
