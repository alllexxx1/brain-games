from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUM = 0
MAX_NUM = 100


def is_prime(number):
    if number % 2 == 0 or number <= 1:
        return False
    elif number == 2:
        return True
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def create_game_data():
    number = randint(MIN_NUM, MAX_NUM)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (number, correct_answer)
