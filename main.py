from board import *

board = ["" for _ in range(9)]

game = TicTacToe(board, 0, True)

is_finished, bot = False, False
empty = 8
turn = "PLAYER"
while not is_finished:
    print(f"========== {turn}'S TURN ==========")
    game.print_board()
    print("-" * 35)
    if not bot:
        idx = int(input("Where to put your symbol? "))
        game.update_board(idx)
        turn = "BOT"
    else:
        idx, _ = game.minimax(empty, True)
        game.update_board(idx)
        turn = "PLAYER"

    bot = not bot
    empty -= 1
    winner, is_finished = game.is_game_finished()


if winner is None:
    print("Huh, it's a tie!")
elif winner == "O":
    print("Oh no, you lose :(")
else:
    print("Congratulations! You win!")
