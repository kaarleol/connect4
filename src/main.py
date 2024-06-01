from main.game import Game
from entities.board import Board

class App:
    def __init__(self):
        self.board = Board()
        self.game = Game(self.board)

    def run(self):
        print("Starting a new game")
        while True:
            self.board.print_board()
            if self.game.check_win():
                break
            if self.board.is_full():
                print("DRAW!")
                break
            
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
            
            

if __name__ == "__main__":
    game = App()
    game.run()