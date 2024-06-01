from entities.game import Game
from entities.board import Board
from entities.ai import AI

class App:
    def __init__(self):
        self.board = Board()
        self.game = Game(self.board)
        self.boardState = self.game.board.get_board()
        self.ai = AI(self.boardState)

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
                    col = input("Give the column you want to place a piece in (0-6)")
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
                self.ai.set_board(self.game.board.get_board())
                move = self.ai.move()
                if move:
                    val = self.game.play(move)
                    if val is False:
                        print("Main: AI tried making an illegal move")
                        break


            
            

if __name__ == "__main__":
    game = App()
    game.run()