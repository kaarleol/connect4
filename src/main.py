import time

from entities.game import Game
from entities.board import Board
from entities.ai import AI


class App:
    def __init__(self):
        self.board = Board()
        self.game = Game(self.board)
        self.board_state = self.game.board.get_board()
        self.ai = AI(self.board_state)
        self.duration = 3 #how long the ai will have to look for best move

    def run(self):
        print("Starting a new game")
        while True:
            self.board.print_board()
            if self.game.check_win():
                break
            if self.board.is_full():
                print("DRAW!")
                break

            turn = self.game.whose_turn()
            if turn == 'X':
                while True:
                    col = input(
                        "Give the column you want to place a piece in (0-6)")
                    try:
                        col = int(col)
                    except ValueError:
                        print(f"Error: '{col}' is not a valid integer")
                        continue

                    if col not in range(7):
                        print("Incorrect column")
                        continue
                    val = self.game.play(col)
                    if val is False:
                        continue
                    break
            if turn == 'O':
                move, val = self.iterative_search()
                print(move, val)
                if move is not None:
                    val = self.game.play(move)
                    if val is False:
                        print("Main: AI tried making an illegal move")
                        break
                else:
                    print("Main: AI failed to return a move")
                    break

    def iterative_search(self):
        print("Starting AI")
        start_time = time.time()
        depth = 1
        move = None

        while time.time() - start_time < self.duration:
            print(f'Depth: {depth}')
            move = self.ai.minimax(self.game.board.get_board(), None, depth, True)
            depth += 1
        return move

if __name__ == "__main__":
    game = App()
    game.run()
