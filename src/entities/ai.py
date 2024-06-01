from entities.board import Board
import random

class AI:
    def __init__(self, boardState):
        self.boardState = boardState
        self.move_values = {'3': 0, '2': 0, '4': 0, '1': 0, '5': 0, '0': 0, '6': 0}
        self.players_move = False
        self.board = Board(boardState)

    def set_board(self, boardState):
        self.boardState = boardState

    def move(self):
        moves = self.board.get_possible_moves()
        for i in moves:
            board = Board(self.boardState)
            self.move_values[str(i)] = self.evaluate_move(board, i)

        best_move = max(self.move_values, key=lambda k: self.move_values[k])
        print(best_move)
        try:
            best_move = int(best_move)
        except:
            print("AI: error making a move")
            return False
        return best_move

    def evaluate_move(self, board, i):
        board.set_piece(i, 'O')
        value = random.uniform(-10, 10)
        if board.check_win('0'):
            value = 1000
        elif board.check_win('X'):
            value = -1000
        print(value)

        return value
