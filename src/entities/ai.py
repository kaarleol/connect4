import time
from entities.board import Board

class AI:
    """
    AI

    The opponent human plays against that uses minimax

    Attributes:
        board_state (list): The current state of the board
        state_best_move (dict): A dictionary storing the best moves for each board state,
        used for move sorting
        board (Board): An instance of the Board class
        duration (int): Duration (in seconds) the AI has to find the best move
    """
    def __init__(self, board_state):
        """
        Initializes a new instance of AI

        Args:
            board_state (list): The boardstate you want AI to play from
        """
        self.board_state = board_state
        self.state_best_move = {}
        self.board = Board(board_state)

        self.duration = 3

    def iterative_search(self, board_state):
        """
        The main method of the AI that the gameloop in main.py calls

        Performs an iterative deepening search to find the best move

        Args:
            board_state (list): The current state of the board

        Returns:
            int: The column index of the best move
        """
        print("Starting AI")
        start_time = time.time()
        depth = 1
        move = None

        while time.time() - start_time < self.duration:
            print(f'Depth: {depth}')
            move, val = self.minimax(board_state, None, depth, -10000000, 10000000, True)
            if val in (0.00000001, 100000, -100000):
                return move, val
            depth += 1

        board = Board(board_state)
        board.set_piece(move, 'O')

        #clearing best moves for the next turn
        self.state_best_move = {}
        #print(self.state_best_move)

        return move, val

    def minimax(self, board_state, column, depth, alpha, beta, maximizing_player):
        """
        Implements the minimax algorithm with alpha-beta pruning

        Args:
            board_state (list): The current state of the board
            column (int): The column where the piece is placed
            depth (int): The current depth of the search
            alpha (float): The alpha value for alpha-beta pruning
            beta (float): The beta value for alpha-beta pruning
            maximizing_player (bool): True if the current player is maximizing, False otherwise

        Returns:
            tuple: The best move and its associated value
        """
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

        if depth == 0:
            evaluation = self.evaluate_move(board.get_board())
            return column, evaluation

        moves = board.get_possible_moves()

        if not moves:
            return column, 0.00000001

        best_value, best_move = -1000000, None

        board_signature = board.get_signature()
        if board_signature in self.state_best_move:
            best_move = self.state_best_move[board_signature]

        if best_move:
            moves.remove(best_move)
            moves = [best_move] + moves

        if maximizing_player:
            best_value = -1000000
            for move in moves:
                _, value = self.minimax(board.get_board(), move, depth - 1, alpha, beta, False)
                if value > best_value:
                    best_value = value
                    best_move = move
                alpha = max(alpha, value)

                self.state_best_move[board_signature] = best_move

                if beta <= alpha:
                    break
        else:
            best_value = 1000000
            for move in moves:
                _, value = self.minimax(board.get_board(), move, depth - 1, alpha, beta, True)
                if value < best_value:
                    best_value = value
                    best_move = move
                beta = min(beta, value)

                self.state_best_move[board_signature] = best_move

                if beta <= alpha:
                    break

        return best_move, best_value

    #the evaluations are my guesses for what could be valuable
    def evaluate_move(self, board_state):
        """
        Evaluates the current board state

        Args:
            board_state (list): The current state of the board

        Returns:
            float: The evaluation score of the board
        """
        heat_chart = [
            [-1, 0, 1, 2, 1, 0, -1],
            [0, 2, 2, 3, 2, 2, 0],
            [0, 2, 5, 7, 5, 2, 0],
            [0, 2, 5, 7, 5, 2, 0],
            [0, 2, 4, 5, 4, 2, 0],
            [0, 1, 2, 4, 2, 1, 0],
        ]

        evaluation = 0
        for i in range(6):
            for j in range(7):
                if board_state[i][j] == "X":
                    evaluation -= heat_chart[i][j]
                if board_state[i][j] == "O":
                    evaluation += heat_chart[i][j]

        evaluation += self.evaluate_open_lines(board_state, 'O')
        evaluation -= self.evaluate_open_lines(board_state, 'X')

        return evaluation

    def evaluate_open_lines(self, board_state, piece):
        '''
        Helper function for evaluate_move

        Evaluates the position of the given player. 
        Checks all directions for connections or open spaces

        Args:
            board_state (list): The current state of the board
            piece ('X' or 'O'): The player whose position is 
        Returns:
            number: The evaluation score of the board

        '''
        if piece == 'O':
            opponent = 'X'
        else:
            opponent = 'O'

        evaluation = 0

        #rows
        for row in range(6):
            for col in range(4):
                partial_eval = 0
                in_a_row = 0
                for i in range(4):
                    if board_state[row][col + i] == piece:
                        in_a_row += 1
                        partial_eval += 2*in_a_row
                    if board_state[row][col + i] == opponent:
                        partial_eval = 0
                        break
                #second player wants rows on every second line in case of endgame
                #rows are read from top to bottom so row=0 in this case would be the 6th row
                if piece == 'O' and row % 2 == 0:
                    partial_eval = partial_eval*2
                if piece == 'X' and (row + 1) == 0:
                    partial_eval = partial_eval*2
                evaluation += partial_eval

        #columns
        for column in range(7):
            for row in range(3):
                partial_eval = 0
                in_a_row = 0
                for i in range(4):
                    if board_state[row + i][column] == piece:
                        in_a_row += 1
                        partial_eval += 2*in_a_row
                    if board_state[row + i][column] == opponent:
                        partial_eval = 0
                        break
                evaluation += partial_eval

        #up-right -diagonal
        for row in range(3,6):
            for column in range(4):
                partial_eval = 0
                in_a_row = 0
                for i in range(4):
                    if board_state[row - i][column + i] == piece:
                        in_a_row += 1
                        partial_eval += 2*in_a_row
                    if board_state[row - i][column + i] == ' ':
                        if (row + i) % 2 == 0 and piece == 'O':
                            partial_eval += 2
                        if (row + i + 1) % 2 == 0 and piece == 'X':
                            partial_eval += 2
                    if board_state[row - i][column + i] == opponent:
                        partial_eval = 0
                        break
                evaluation += partial_eval

        #down-right -diagonal
        for row in range(3):
            for column in range(4):
                in_a_row = 0
                partial_eval = 0
                for i in range(4):
                    if board_state[row + i][column + i] == piece:
                        in_a_row += 1
                        partial_eval += 2*in_a_row
                    if board_state[row + i][column + i] == ' ':
                        if (row + i) % 2 == 0 and piece == 'O':
                            partial_eval += 2
                        if (row + i + 1) % 2 == 0 and piece == 'X':
                            partial_eval += 2
                    if board_state[row + i][column + i] == opponent:
                        partial_eval = 0
                        break
                evaluation += partial_eval

        return evaluation
