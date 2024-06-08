import unittest
from entities.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.test_board = Board()

    def test_board_sets_up_empty_board(self):
        self.assertEqual(len(self.test_board.get_board()), 6)
        self.assertEqual(len(self.test_board.get_board()[0]), 7)
        
        board = self.test_board.get_board()

        for i in range(6):
            for j in range(7):
                self.assertEqual(board[i][j], ' ')