from random import randint


rules = 'Find the greatest common divisor of given numbers.'


def initialize_game():
    first_number = randint(0, 50)
    second_number = randint(0, 50)
    question = f'{first_number} {second_number}'
    result = 0
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    result += (first_number + second_number)
    return (question, str(result))
