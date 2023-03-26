from random import randint


rules = 'What number is missing in the progression?'


def initialize_game():
    progression = list(range(randint(0, 10), randint(30, 40), randint(2, 6)))
    hidden_index = randint(0, len(progression) - 1)
    right_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, right_answer
