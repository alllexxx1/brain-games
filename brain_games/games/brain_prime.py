from random import randint


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number % 2 == 0 or number <= 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True


def initialize_game():
    number = randint(0, 100)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (number, correct_answer)
