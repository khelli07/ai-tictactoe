MAX_VAL = 10


class TicTacToe:
    def __init__(self, board, depth, is_x, parent=None, move=None):
        self.board = board
        self.depth = depth

        self.is_x = is_x
        self.symbol = "X" if is_x else "O"

        self.children = []
        self.parent = parent
        self.move = move

    def print_board(self):
        for i in range(9):
            if self.board[i] != "":
                print(self.board[i], end=" ")
            else:
                print("-", end=" ")

            if (i + 1) % 3 == 0:
                print(f"\t{i - 2} {i - 1} {i}")

    def minimax(self, depth, maxi, alpha=-MAX_VAL, beta=MAX_VAL):
        winner, is_finished = self.is_game_finished()

        if is_finished:
            move, symbol = self._get_root_info()
            return move, self.calculate_game_score(winner, symbol)

        opt_score = -MAX_VAL if maxi else MAX_VAL
        next_opt_move = None
        self._make_children()
        i = 1
        for child in self.children:
            move, score = child.minimax(depth - 1, not maxi, alpha, beta)
            if maxi:
                if opt_score < score:
                    opt_score = score
                    next_opt_move = move
                alpha = max(alpha, opt_score)
            else:
                if opt_score > score:
                    opt_score = score
                    next_opt_move = move
                beta = min(beta, opt_score)

            i += 1
            if beta <= alpha:
                break

        return next_opt_move, opt_score

    def calculate_game_score(self, winner, player_symbol):
        if winner is None:
            return 0
        elif winner == player_symbol:
            return 1 + self.depth
        else:
            return -1

    def is_game_finished(self):
        arr = self.board

        # check across
        for i in range(0, 9, 3):
            if arr[i] == arr[i + 1] and arr[i] == arr[i + 2] and arr[i] != "":
                return arr[i], True

        # check down
        for i in range(3):
            if arr[i] == arr[i + 3] and arr[i] == arr[i + 6] and arr[i] != "":
                return arr[i], True

        # check diagonal
        if arr[0] == arr[4] and arr[0] == arr[8] and arr[0] != "":
            return arr[0], True

        if arr[2] == arr[4] and arr[2] == arr[6] and arr[2] != "":
            return arr[2], True

        # check if draw
        if self._is_board_full():
            return None, True

        return None, False

    def update_board(self, idx):
        self._put_symbol(idx)
        self._update_game_state()

    def _put_symbol(self, idx):
        if self.board[idx] != "":
            raise ValueError("That place has been taken!")
        self.board[idx] = self.symbol
        self._change_player()

    def _update_game_state(self):
        self.depth += 1
        self.children = []
        self.parent = None
        self.move = None

    def _change_player(self):
        self.is_x = not self.is_x
        self.symbol = "X" if self.is_x else "O"

    def _make_children(self):
        for i in range(9):
            if self.board[i] == "":
                child = TicTacToe(
                    [sym for sym in self.board], self.depth + 1, self.is_x, self, i
                )
                child._put_symbol(i)
                self.children.append(child)

    def _is_board_full(self):
        for i in range(9):
            if self.board[i] == "":
                return False

        return True

    def _get_root_info(self):
        cr = self
        while cr.parent.move is not None:
            cr = cr.parent
        return cr.move, cr.parent.symbol
