class Board:
    """
    Board

    Represents a Connect Four game board.

    Attributes:
        board (list): A 6x7 matrix representing the board state.
    """
    def __init__(self, preset_board=None):
        """
        Initializes a new instance of the Board.

        Args:
            preset_board (list, optional): A predefined board state. 
            If not provided, initializes an empty board.
        """
        if preset_board:
            self.board = preset_board
        else:
            self.board = [[' ' for _ in range(7)] for _ in range(6)]

    def print_board(self):
        """
        Prints the current board state to the console.
        """
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')
        print('-' * (len(self.board[0]) * 4 + 1))
        print('  0   1   2   3   4   5   6  ')

    def set_piece(self, col, piece):
        """
        Sets a piece in the specified column.

        Args:
            col (int): The column index (0-6).
            piece (str): The piece to set ('X' or 'O').

        Returns:
            bool: True if the piece was set successfully, False otherwise.
        """
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
        """
        Checks if the specified piece has won the game.

        Args:
            piece (str): The piece to check for a win ('X' or 'O').

        Returns:
            bool: True if the specified piece has a winning line, False otherwise.
        """
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
        """
        Checks if the board is full.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def is_column_full(self, col):
        """
        Checks if the specified column is full.

        Args:
            col (int): The column index (0-6).

        Returns:
            bool: True if the column is full, False otherwise.
        """
        if col not in range(7):
            print("Board: Incorrect column")
            return False
        for row in self.board:
            if row[col] == ' ':
                return False
        return True

    def get_possible_moves(self):
        """
        Gets a list of possible moves, ordered by preference.

        Returns:
            list: A list of column indices where a piece can be placed.
        """
        move_order = [3,4,2,5,1,6,0]
        possible_moves = []
        for col in move_order:
            if not self.is_column_full(col):
                possible_moves.append(col)
        return possible_moves

    def get_board(self):
        """
        Gets a copy of the current board state.

        Returns:
            list: A copy of the board state.
        """
        return [row[:] for row in self.board]

    def set_board(self, board_state):
        """
        Sets the board state to the provided state.

        Args:
            board_state (list): A new board state to set.
        """
        self.board = board_state

    def get_signature(self):
        """
        Gets a string representation (signature) of the current board state.

        Returns:
            str: A string representation of the board state.
        """
        signature = ''
        for row in self.board:
            for column in row:
                signature += column

        return signature
