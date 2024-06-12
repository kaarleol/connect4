import random
from entities.board import Board


class AI:
    def __init__(self, board_state):
        self.board_state = board_state
        self.move_values = {'3': 0, '2': 0,
                            '4': 0, '1': 0, '5': 0, '0': 0, '6': 0}
        self.board = Board(board_state)


    def set_board(self, board_state):
        self.board_state = board_state

    def minimax(self, board_state, column, depth, maximizing_player):

        board = Board(board_state)
        board.set_board(board.get_board())

        if maximizing_player is False:
            if column is not None:
                board.set_piece(column, 'O')
                if board.check_win('O'):
                    return column, 100000
        else:
            if column is not None:
                board.set_piece(column, 'X')
                if board.check_win('X'):
                    return column, -100000

        board.set_board(board.get_board())

        if depth == 0:
            evaluation = self.evaluate_move(board.get_board())
            return column, evaluation

        moves = board.get_possible_moves()

        if not moves:
            return column, 0

        best_value, best_move = -1000000, None

        if maximizing_player:
            best_value = -1000000
            for move in moves:
                _, value = self.minimax(board.get_board(), move, depth - 1, False)
                if value > best_value:
                    best_value = value
                    best_move = move
            return best_move, best_value
        else:
            best_value = 1000000
            for move in moves:
                _, value = self.minimax(board.get_board(), move, depth - 1, True)
                if value < best_value:
                    best_value = value
                    best_move = move
            return best_move, best_value

    def evaluate_move(self, board_state):
        heat_chart = [
            [-1,0,1,2,1,0,-1],
            [0,2,2,3,2,2,0],
            [0,2,5,7,5,2,0],
            [0,2,5,7,5,2,0],
            [0,2,4,5,4,2,0],
            [0,1,2,4,2,1,0],
        ]
        board = Board(board_state)

        evaluation = 0
        for i in range(6):
            for j in range(7):
                if board_state[i][j]== "X":
                    evaluation -= heat_chart[i][j]
                if board_state[i][j] == "O":
                    evaluation += heat_chart[i][j]

        if board.check_win('X'):
            return -100000
        elif board.check_win('O'):
            return 100000

        #some randomness to mix up the gameplay
        return evaluation + random.uniform(-2, 2)
