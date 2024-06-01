class Board:
    def __init__(self):
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