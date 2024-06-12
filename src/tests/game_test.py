import unittest
from unittest.mock import patch
from entities.board import Board
from entities.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.test_board = Board()
        self.test_game = Game(self.test_board)

    def test_game_inits_correctly_with_empty_board(self):
        self.assertEqual(self.test_game.turn, 0)

        board_State = self.test_game.board.get_board()

        for i in range(6):
            for j in range(7):
                self.assertEqual(board_State[i][j], ' ')

    def test_game_playes_correct_moves_and_pieces(self):
        self.test_game.play(3)
        self.test_game.play(3)
        self.test_game.play(3)

        self.assertEqual(self.test_game.board.get_board(),[
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ','X',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','X',' ',' ',' ',],
        ])

    def test_turn_ticks_correctly(self):
        self.test_game.play(3)
        self.test_game.play(3)
        self.test_game.play(3)
        self.test_game.play(3)
        self.test_game.play(3)

        self.assertEqual(self.test_game.turn, 5)

    def test_player_changes_correctly(self):
        self.assertEqual(self.test_game.whose_turn(), 'X')

        self.test_game.play(3)
        self.assertEqual(self.test_game.whose_turn(), 'O')

        self.test_game.play(3)
        self.assertEqual(self.test_game.whose_turn(), 'X')

    def test_game_checks_for_correct_players_win(self):
        board_preset = [
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ','X','X','X',' ',' ',' ',],
        ]

        self.test_game.board.set_board(board_preset)
        self.assertEqual(self.test_game.check_win(), False)
        self.test_game.play(4)
        self.assertEqual(self.test_game.check_win(), True)

    @patch('builtins.print')
    def test_game_announces_correct_winner(self, mock_print):
        board_preset = [
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ','X','X','X',' ',' ',' ',],
        ]
        self.test_game.board.set_board(board_preset)

        val = self.test_game.check_win()

        self.assertEqual(val, False)
        self.assertEqual(mock_print.call_count, 0)
        
        self.test_game.play(4)

        val = self.test_game.check_win()

        self.assertEqual(mock_print.call_count, 1)

    @patch('builtins.print')
    def test_game_announces_o_as_winner(self, mock_print):
        board_preset = [
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ',' ',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ','X','X','X',' ',' ',' ',],
        ]
        self.test_game.board.set_board(board_preset)

        val = self.test_game.check_win()

        self.assertEqual(val, False)
        self.assertEqual(mock_print.call_count, 0)
        
        self.test_game.play(5)
        val = self.test_game.check_win()
        self.assertEqual(val, False)

        self.assertEqual(mock_print.call_count, 0)

        self.test_game.play(3)

        val = self.test_game.check_win()

        self.assertEqual(val, True)
        self.assertEqual(mock_print.call_count, 1)

    def test_full_column_returns_false(self):
        board_preset = [
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','X',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ',' ',' ','O',' ',' ',' ',],
            [' ','X','X','X',' ',' ',' ',],
        ]
        self.test_game.board.set_board(board_preset)

        val = self.test_game.play(3)

        self.assertEqual(val, False)