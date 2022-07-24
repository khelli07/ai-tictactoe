import argparse
from board import *

parser = argparse.ArgumentParser(description="Tic-Tac-Toe")
parser.add_argument(
    "-b", "--bot", action="store_true", help="This flag specify if bot starts first"
)
args = parser.parse_args()

game = TicTacToe(["" for _ in range(9)], 0, True)

is_finished, bot = False, bool(vars(args)["bot"])
empty = 8
while not is_finished:
    if not bot:
        game.print_board()
        print("-" * 35)
        idx = int(input("Where to put your symbol? "))
        game.update_board(idx)
    else:
        idx, _ = game.minimax(empty, True)
        game.update_board(idx)

    bot = not bot
    empty -= 1
    winner, is_finished = game.is_game_finished()


if winner is None:
    print("Huh, it's a tie!")
elif winner == "O":
    print("Oh no, you lose :(")
else:
    print("Congratulations! You win!")
