from entities.board import Board
import random

class AI:
    def __init__(self, board_state):
        self.board_state = board_state
        self.move_values = {'3': 0, '2': 0,
                            '4': 0, '1': 0, '5': 0, '0': 0, '6': 0}
        self.board = Board(board_state)

    def set_board(self, board_state):
        self.board_state = board_state

    def move(self, board_state, depth):
        board = Board(board_state)
        moves = board.get_possible_moves()

        best_value, best_move = -1000000, None
        for move in moves:
            value = self.minimax(board_state, move, depth-1, True)
            print(f'move {move} value {value}')
            if value > best_value:
                best_value = value
                best_move = move
        return best_move

    def minimax(self, board_state, column, depth, maximizing_player):
        board = Board(board_state)
        board.set_board(board.get_board())
        if maximizing_player:
            board.set_piece(column, 'O')
        else:
            board.set_piece(column, 'X')

        board.set_board(board.get_board())

        if depth == 0 or board.check_win('X') or board.check_win('O'):
            eval = self.evaluate_move(board.get_board())
            return eval
        moves = board.get_possible_moves()

        if not moves:
            return 0

        if maximizing_player is False:
            best_value = -1000000
            for move in moves:
                value = self.minimax(board.get_board(), move, depth - 1, True)
                print(f'AI:s move: value for move {move} is {value}')
                if value > best_value:
                    best_value = value
            return best_value
        else:
            best_value = 1000000
            for move in moves:
                value = self.minimax(board.get_board(), move, depth - 1, False)
                print(f'Players move: value for move {move} is {value}')
                if value < best_value:
                    best_value = value
            return best_value

    def evaluate_move(self, board_state):
        board = Board(board_state)
        board.set_board(board.get_board())

        if board.check_win('X'):
            print("player would win")
            return -100000
        elif board.check_win('O'):
            print("ai would win")
            return 100000

        return random.uniform(-10, 10)
