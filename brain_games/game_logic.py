import prompt


def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.rules)
    right_answers = 3
    while right_answers:
        question, correct_answer = game.initialize_game()
        print(f'Question: {question}')
        user_answer = prompt.string('You answer: ')
        if user_answer != correct_answer:
            print(f'"{user_answer}" is wrong answer ;(.'
                  f'Correct answer was "{correct_answer}".\n'
                  f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
            right_answers -= 1
    else:
        print(f'Congratulations, {name}!')
