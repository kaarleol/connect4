import unittest
from unittest.mock import patch
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

    def test_set_board_with_preset_board(self):
        board_preset = [
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','X',' ',' ',' ',],
            [' ',' ','O','O',' ',' ',' ',],
            [' ','X','X','X',' ',' ',' ',],
        ]

        board = Board(board_preset)

        board_state = board.get_board()

        self.assertEqual(board_state[5][1], 'X')
        self.assertEqual(board_state[4][3], 'O')

    def test_board_set_piece(self):
        self.test_board.set_piece(3, 'X')
        board_state = self.test_board.get_board()

        self.assertEqual(board_state[5][3], 'X')

    def test_board_set_piece_with_two_pieces(self):
        self.test_board.set_piece(3, 'X')
        self.test_board.set_piece(3, 'O')
        board_state = self.test_board.get_board()

        self.assertEqual(board_state[5][3], 'X')
        self.assertEqual(board_state[4][3], 'O')

    def test_board_set_piece_with_incorrect_piece(self):
        val = self.test_board.set_piece(3, 'Y')

        self.assertEqual(val, False)

    def test_board_set_piece_with_incorrect_column(self):
        val = self.test_board.set_piece(7, 'X')

        self.assertEqual(val, False)

    def test_board_is_column_full_with_full_column(self):
        board_preset = [
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','X',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','X',' ',' ',' ',],
            [' ',' ','O','O',' ',' ',' ',],
            [' ','X','X','X',' ',' ',' ',],
        ]
        board = Board(board_preset)
        val = board.is_column_full(3)
        self.assertEqual(val, True)

    def test_board_is_column_full_with_wrong_column(self):
        board_preset = [
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','X',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','X',' ',' ',' ',],
            [' ',' ','O','O',' ',' ',' ',],
            [' ','X','X','X',' ',' ',' ',],
        ]
        board = Board(board_preset)
        val = board.is_column_full(7)
        self.assertEqual(val, False)

    def test_board_is_column_full_with_not_full_column(self):
        board_preset = [
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ','X',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','X',' ',' ',' ',],
            [' ',' ','O','O',' ',' ',' ',],
            [' ','X','X','X',' ',' ',' ',],
        ]
        board = Board(board_preset)
        val = board.is_column_full(3)
        self.assertEqual(val, False)

    def test_board_set_piece_with_full_column(self):
        board_preset = [
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','X',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','X',' ',' ',' ',],
            [' ',' ','O','O',' ',' ',' ',],
            [' ','X','X','X',' ',' ',' ',],
        ]

        board = Board(board_preset)
        val = board.set_piece(3, 'O')

        self.assertEqual(val, False)

    def test_get_possible_moves_with_empty_board(self):
        moves = self.test_board.get_possible_moves()

        self.assertEqual(len(moves), 7)
        
    def test_get_possible_moves_with_some_full_columns(self):
        board_preset = [
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ','O','X',' ',' ',' ',],
            [' ',' ','X','O',' ',' ',' ',],
            [' ',' ','O','X',' ',' ',' ',],
            [' ',' ','O','O',' ',' ',' ',],
            [' ','X','X','X',' ',' ',' ',],
        ]

        board = Board(board_preset)
        moves = board.get_possible_moves()

        self.assertEqual(len(moves), 6)

        board.set_piece(2,'X')
        moves = board.get_possible_moves()
        self.assertEqual(len(moves), 5)

    def test_is_board_full(self):
        board_preset = [
            ['X','O','O','O','X','O','O',],
            ['O','X','X','X','O','X','X',],
            ['X','O','O','O','X','O','O',],
            ['O','X','X','X','O','X','X',],
            ['X','O','O','O','X','O','O',],
            ['O','X','X','X','O','X','X',],
        ]

        board = Board(board_preset)
        val = board.is_full()
        self.assertEqual(val, True)

    def test_is_board_full_with_non_full_board(self):
        board_preset = [
            ['X','O','O','O','X','O',' ',],
            ['O','X','X','X','O','X','X',],
            ['X','O','O','O','X','O','O',],
            ['O','X','X','X','O','X','X',],
            ['X','O','O','O','X','O','O',],
            ['O','X','X','X','O','X','X',],
        ]

        board = Board(board_preset)
        val = board.is_full()
        self.assertEqual(val, False)

    def test_board_set_board(self):
        board_preset = [
            ['X','O','O','O','X','O','O',],
            ['O','X','X','X','O','X','X',],
            ['X','O','O','O','X','O','O',],
            ['O','X','X','X','O','X','X',],
            ['X','O','O','O','X','O','O',],
            ['O','X','X','X','O','X','X',],
        ]
        self.test_board.set_board(board_preset)

        board_state = self.test_board.get_board()

        self.assertEqual(board_state, board_preset)

    def test_check_win_with_no_winner(self):
        board_preset = [
            ['X','O','O','O','X','O','O',],
            ['O','X','X','X','O','X','X',],
            ['X','O','O','O','X','O','O',],
            ['O','X','X','X','O','X','X',],
            ['X','O','O','O','X','O','O',],
            ['O','X','X','X','O','X','X',],
        ]
        self.test_board.set_board(board_preset)

        self.assertEqual(self.test_board.check_win('X'), False)
        self.assertEqual(self.test_board.check_win('O'), False)

    def test_check_win_with_x_winning(self):
        board_preset = [
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ','O','X',' ',' ',' ',],
            [' ',' ','X','O',' ',' ',' ',],
            [' ',' ','O','X',' ',' ',' ',],
            [' ','O','O','O',' ',' ',' ',],
            [' ','X','X','X','X',' ',' ',],
        ]

        self.test_board.set_board(board_preset)

        self.assertEqual(self.test_board.check_win('X'), True)
        self.assertEqual(self.test_board.check_win('O'), False)

    def test_check_win_with_o_winning(self):
        board_preset = [
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ','X','X','X',' ','X',' ',],
        ]

        self.test_board.set_board(board_preset)

        self.assertEqual(self.test_board.check_win('X'), False)
        self.assertEqual(self.test_board.check_win('O'), True)

    def test_check_win_with_up_right_diagonal_win(self):
        board_preset = [
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ','X',' ',],
            [' ',' ',' ',' ','X','X',' ',],
            [' ',' ',' ','X','O','O',' ',],
            [' ',' ','X','O','O','X','O',],
        ]

        self.test_board.set_board(board_preset)

        self.assertEqual(self.test_board.check_win('X'), True)
        self.assertEqual(self.test_board.check_win('O'), False)

    def test_check_win_with_down_right_diagonal_win(self):
        board_preset = [
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ','O',' ','',' ',],
            [' ',' ',' ','X','O','',' ',],
            [' ',' ',' ','X','O','O',' ',],
            [' ',' ','O','X','X','X','O',],
        ]

        self.test_board.set_board(board_preset)

        self.assertEqual(self.test_board.check_win('X'), False)
        self.assertEqual(self.test_board.check_win('O'), True)

    @patch('builtins.print')
    def test_print_called(self, mock_print):
        self.test_board.print_board()
        self.assertEqual(mock_print.call_count, 7)