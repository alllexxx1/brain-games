from random import randint
from math import gcd


RULE = 'Find the greatest common divisor of given number.'
MIN_FIRST_NUM = 0
MAX_FIRST_NUM = 50
MIN_SECOND_NUM = 0
MAX_SECOND_NUM = 50


def create_game_data():
    first_number = randint(MIN_FIRST_NUM, MAX_FIRST_NUM)
    second_number = randint(MIN_SECOND_NUM, MAX_SECOND_NUM)
    result = gcd(first_number, second_number)
    question = f'{first_number} {second_number}'
    return (question, str(result))
