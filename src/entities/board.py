class Board:
    def __init__(self, preset_board=None):
        if preset_board:
            self.board = preset_board
        else:
            self.board = [[' ' for _ in range(7)] for _ in range(6)]

    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')
        print('-' * (len(self.board[0]) * 4 + 1))

    def set_piece(self, col, piece):
        if piece not in ['X', 'O']:
            print("Board: Error setting a piece")
            return False
        if col not in range(7):
            print("Board: Incorrect column")
            return False

        for row in reversed(self.board):
            if row[col] == ' ':
                row[col] = piece
                return True

        print("Board: Column is full")
        return False

    def check_win(self, piece):
        # Check rows for win
        for row in range(6):
            for col in range(4):
                if all(self.board[row][col+i] == piece for i in range(4)):
                    return True

        # Check columns for win
        for col in range(7):
            for row in range(3):
                if all(self.board[row+i][col] == piece for i in range(4)):
                    return True

        # Check up-right diagonal
        for row in range(3):
            for col in range(4):
                if all(self.board[row+i][col+i] == piece for i in range(4)):
                    return True

        # Check down-right diagonal
        for row in range(3, 6):
            for col in range(4):
                if all(self.board[row-i][col+i] == piece for i in range(4)):
                    return True

        return False

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def is_column_full(self, col):
        if col not in range(7):
            print("Board: Incorrect column")
            return False
        for row in self.board:
            if row[col] == ' ':
                return False
        return True

    def get_possible_moves(self):
        move_order = [3,4,2,5,1,6,0]
        possible_moves = []
        for col in move_order:
            if not self.is_column_full(col):
                possible_moves.append(col)
        return possible_moves

    def get_board(self):
        return [row[:] for row in self.board]

    def set_board(self, board_state):
        self.board = board_state

    def get_signature(self):
        signature = ''
        for row in self.board:
            for column in row:
                signature += column    

        return signature