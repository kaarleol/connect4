class Game:
    def __init__(self, board):
        self.board = board
        self.turn = 0

    def play(self, column):
        piece = self.whose_turn()

        val = self.board.set_piece(column, piece)
        if not val:
            return False

        self.turn += 1

    def check_win(self):
        piece = self.whose_turn()
        if self.board.check_win(piece):
            print(f'Player {piece} wins!')
            return True
        return False

    def whose_turn(self):
        if self.turn % 2 == 0:
            piece = 'X'
        else:
            piece = 'O'
        return piece
