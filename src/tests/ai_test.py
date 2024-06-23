import unittest
from unittest.mock import patch
from entities.board import Board
from entities.ai import AI

#Note: Some tests have timers for the ai. If for some reason tests do not finish try increasing duration within the test that fails
#Example: self.test_ai.duration = 3
#Timer in seconds.

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.test_board = Board()
        self.test_ai = AI(self.test_board.get_board())

    def test_ai_sets_up_empty_board_and_dict(self):
        self.assertEqual(len(self.test_ai.board.get_board()), 6)
        self.assertEqual(len(self.test_ai.board.get_board()[0]), 7)
        self.assertEqual(len(self.test_ai.state_best_move), 0)

        board = self.test_ai.board.get_board()

        for i in range(6):
            for j in range(7):
                self.assertEqual(board[i][j], ' ')

    
    def test_minimax_finds_depth_1_win(self):
        board_preset = [
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ','',' ',],
            [' ',' ',' ','X','O','',' ',],
            [' ',' ',' ','X','O','O',' ',],
            [' ',' ','O','X','X','X','O',],
        ]

        move, value = self.test_ai.minimax(board_preset, None, 1, -10000000, 10000000, True)
        self.assertEqual(move, 3)
        self.assertEqual(value, 100000)

    def test_minimax_prevents_open_three(self):
        board_preset = [
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','X','X',' ',' ',],
        ]

        move, value = self.test_ai.minimax(board_preset, None, 4, -10000000, 10000000, True)
        self.assertEqual(True, move in [2, 5])

    def test_minimax_finds_forced_win_in_4(self):
        board_preset = [
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','X',' ',' ',' ',],
            [' ',' ',' ','O',' ','X',' ',],
            [' ',' ','X','X',' ','O',' ',],
            [' ','X','X','O',' ','O',' ',],
            [' ','X','O','X','X','O','O',],
        ]

        move, value = self.test_ai.minimax(board_preset, None, 4, -10000000, 10000000, True)
        self.assertEqual(True, move in [4, 6])
        self.assertEqual(value, 100000)

    def test_minimax_finds_late_game_draw(self):
        board_preset = [
            [' ',' ','X','O',' ','O',' ',],
            [' ',' ','O','X',' ','X',' ',],
            [' ','X','O','O',' ','X',' ',],
            [' ','O','X','X',' ','O','X',],
            [' ','O','X','O',' ','O','X',],
            ['X','X','O','X','X','O','O',],
        ]

        move, value = self.test_ai.minimax(board_preset, None, 16, -10000000, 10000000, True)
        self.assertEqual(True, move in [0, 1])
        self.assertEqual(value, 0.00000001)

    def test_evaluation_checks_all_corners(self):
        board_preset = [
            ['O',' ',' ',' ',' ',' ','O',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            ['O',' ',' ',' ',' ',' ','O',],
        ]
        board_preset1 = [
            [' ',' ',' ',' ',' ',' ','O',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            ['O',' ',' ',' ',' ',' ','O',],
        ]
        board_preset2 = [
            ['O',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            ['O',' ',' ',' ',' ',' ','O',],
        ]
        board_preset3 = [
            ['O',' ',' ',' ',' ',' ','O',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ','O',],
        ]
        board_preset4 = [
            ['O',' ',' ',' ',' ',' ','O',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            ['O',' ',' ',' ',' ',' ',' ',],
        ]
        evaluation = self.test_ai.evaluate_move(board_preset)
        evaluation1 = self.test_ai.evaluate_move(board_preset1)
        evaluation2 = self.test_ai.evaluate_move(board_preset2)
        evaluation3 = self.test_ai.evaluate_move(board_preset3)
        evaluation4 = self.test_ai.evaluate_move(board_preset4)
        self.assertEqual(True, (evaluation > evaluation1 and evaluation > evaluation2 and
                                evaluation > evaluation3 and evaluation > evaluation4))

    def test_iterative_search_finds_win_in_3(self):
        self.test_ai.duration = 3
        board_preset = [
            [' ',' ',' ','O','X',' ',' ',],
            [' ','O',' ','X','O',' ',' ',],
            [' ','X',' ','O','X',' ','O',],
            [' ','X',' ','X','O','O','X',],
            [' ','O',' ','O','X','O','X',],
            [' ','O','X','X','O','X','X',],
        ]
        move, val = self.test_ai.iterative_search(board_preset)
        self.assertEqual(move, 5)
        self.assertEqual(val, 100000)

    def test_ai_also_detects_its_loss(self):
        self.test_ai.duration = 1
        board_preset = [
            [' ',' ',' ','X','O',' ',' ',],
            [' ','x',' ','O','X',' ',' ',],
            [' ','O',' ','X','O','X','X',],
            [' ','O',' ','O','X','X','O',],
            [' ','X',' ','X','O','X','O',],
            [' ','X','O','O','X','O','O',],
        ]

        _, val = self.test_ai.iterative_search(board_preset)
        self.assertEqual(val, -100000)