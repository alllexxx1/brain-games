from random import randint, choice


rules = 'What is the result of the expression?'


def initialize_game():
    first_operand = randint(10, 20)
    second_operand = randint(0, 10)
    operator = ('+', '-', '*')
    operator = choice(operator)
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
