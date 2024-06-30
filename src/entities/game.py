class Game:
    """
    Game

    Represents a Connect Four game, managing the gameplay and turns.

    Attributes:
        board (Board): The game board.
        turn (int): The current turn number.
    """
    def __init__(self, board):
        """
        Initializes a new instance of the Game.

        Args:
            board (Board): The game board.
        """
        self.board = board
        self.turn = 0

    def play(self, column):
        """
        Plays a piece in the specified column.

        Args:
            column (int): The column index (0-6).

        Returns:
            bool: True if the piece was placed successfully, False otherwise.
        """
        piece = self.whose_turn()

        val = self.board.set_piece(column, piece)
        if not val:
            return False

        self.turn += 1
        return True

    def check_win(self):
        """
        Checks if there is a winner.

        Returns:
            bool: True if there is a winner, False otherwise.
        """
        if self.board.check_win('X'):
            print('Player X wins!')
            return True
        if self.board.check_win('O'):
            print('Player O wins!')
            return True
        return False

    def whose_turn(self):
        """
        Determines whose turn it is to play.

        Returns:
            str: 'X' if it's Player X's turn, 'O' if it's Player O's turn.
        """
        if self.turn % 2 == 0:
            piece = 'X'
        else:
            piece = 'O'
        return piece
