from random import randint


RULE = 'What number is missing in the progression?'
MIN_FIRST_NUM = 0
MAX_FIRST_NUM = 5
MIN_SECOND_NUM = 30
MAX_SECOND_NUM = 40
MIN_STEP = 2
MAX_STEP = 6


def create_game_data():
    progression = list(range(randint(MIN_FIRST_NUM, MAX_FIRST_NUM),
                             randint(MIN_SECOND_NUM, MAX_SECOND_NUM),
                             randint(MIN_STEP, MAX_STEP)))
    hidden_index = randint(0, len(progression) - 1)
    right_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, right_answer
