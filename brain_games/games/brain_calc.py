from random import randint, choice


RULE = 'What is the result of the expression?'
MIN_FIRST_OPERAND = 10
MAX_FIRST_OPERAND = 20
MIN_SECOND_OPERAND = 0
MAX_SECOND_OPERAND = 10
OPERATORS = ('+', '-', '*')


def create_game_data():
    first_operand = randint(MIN_FIRST_OPERAND, MAX_FIRST_OPERAND)
    second_operand = randint(MIN_SECOND_OPERAND, MAX_SECOND_OPERAND)
    operator = choice(OPERATORS)
    expression = f'{first_operand} {operator} {second_operand}'
    result = 0
    match operator:
        case '+':
            result = first_operand + second_operand
        case '-':
            result = first_operand - second_operand
        case '*':
            result = first_operand * second_operand
    return (expression, str(result))
