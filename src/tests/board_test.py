import unittest
from entities.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.test_board = Board()

    def test_board_sets_up_correctly(self):
        self.assertEqual(len(self.test_board.get_board()[0]), 7)