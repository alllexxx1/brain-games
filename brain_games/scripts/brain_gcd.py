#!usr/bin/env python3


from brain_games import game_logic
from brain_games.games import brain_gcd


def main():
    game_logic.play(brain_gcd)


if __name__ == '__main__':
    main()
