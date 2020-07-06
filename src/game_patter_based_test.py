from unittest import TestCase
import unittest
from game_pattern_based import GamePatternBased


# patter based game
patter_game_winner_X_row = {(0,0): 'X', (2,2): 'O', (0,2): 'X', (2,1): 'O', (0,1): 'X'}
patter_game_winner_X_column = {(0,0): 'X', (2,2): 'O', (2,0): 'X', (2,1): 'O', (1,0): 'X'}
patter_game_winner_X_diagonal = {(0,0): 'X', (2,1): 'O', (2,2): 'X', (2,1): 'O', (1,1): 'X'}

patter_game_winner_O_row = {(0,0): 'X', (1,0): 'O', (2,0): 'X', (1,1): 'O', (0,1): 'X', (1,2): 'O'}
patter_game_winner_O_column = {(0,0): 'X', (0,1): 'O', (1,0): 'X', (1,1): 'O', (2,0): 'X', (2,1): 'O'}
patter_game_winner_O_diagonal = {(0,0): 'X', (2,0): 'O', (1,0): 'X', (1,1): 'O', (0,1): 'X', (0,2): 'O'}

patter_game_winner_draw = {(0,0): 'X', (0,1): 'O', (0,2): 'X', (1,0): 'O', (1,1): 'X',
                            (1,2): 'O', (2,0): 'X', (2,1): 'O', (2,2): 'X'}

patter_game_continue = {(0,0): 'X', (2,2): 'O'}

patter_not_allow_update = {(0,0): 'X', (0,1): 'O'}


class TicTacToeGameTestCase(TestCase):

    def setUp(self):
        self.game_object = GamePatternBased('T')

    def run_test(self, given_answer, expected_out):
        """

        :param given_answer:
        :param expected_out:
        :return:
        """
        self.assertEqual(given_answer, expected_out)

    def test_winner_X_row(self):
        """

        test case to check X is the winner for winner_X input
        :return:
        """
        self.game_object.board_dict = patter_game_winner_X_row
        result, _ = self.game_object.based_win_condition()
        self.run_test((result.format("X"), _), ('Won (The player X has met the criteria for win)', False))

    def test_winner_X_column(self):
        """

        test case to check X is the winner for winner_X input
        :return:
        """
        self.game_object.board_dict = patter_game_winner_X_column
        result, _ = self.game_object.based_win_condition()
        self.run_test((result.format("X"), _), ('Won (The player X has met the criteria for win)', False))

    def test_winner_X_diagonal(self):
        """

        test case to check X is the winner for winner_X input
        :return:
        """
        self.game_object.board_dict = patter_game_winner_X_diagonal
        result, _ = self.game_object.based_win_condition()
        self.run_test((result.format("X"), _), ('Won (The player X has met the criteria for win)', False))

    def test_winner_O_row(self):
        """

        test case to check X is the winner for winner_X input
        :return:
        """
        self.game_object.board_dict = patter_game_winner_O_row
        result, _ = self.game_object.based_win_condition()
        self.run_test((result.format("O"), _), ('Won (The player O has met the criteria for win)', False))

    def test_winner_O_column(self):
        """

        test case to check X is the winner for winner_X input
        :return:
        """
        self.game_object.board_dict = patter_game_winner_O_column
        result, _ = self.game_object.based_win_condition()
        self.run_test((result.format("O"), _), ('Won (The player O has met the criteria for win)', False))

    def test_winner_O_diagonal(self):
        """

        test case to check X is the winner for winner_X input
        :return:
        """
        self.game_object.board_dict = patter_game_winner_O_diagonal
        result, _ = self.game_object.based_win_condition()
        self.run_test((result.format("O"), _), ('Won (The player O has met the criteria for win)', False))

    def test_patter_game_draw(self):
        """

        test case to check the game is draw
        :return:
        """
        self.game_object.board_dict = patter_game_winner_draw
        empty_block = self.game_object.is_empty_poisiton()
        self.run_test(empty_block, 0)

    def test_patter_game_continue(self):
        """

        test case to check the game will continue
        :return:
        """
        self.game_object.board_dict = patter_game_continue
        result, _ = self.game_object.based_win_condition()
        self.run_test((result, _), ("Continue (The game should continue)", True))

    def test_patter_game_update_existing(self):
        """

        test case to check we can't update existing
        :return:
        """
        board_dict, flag = GamePatternBased.update_board_dict(0, 1, 'X', patter_not_allow_update)
        self.run_test((board_dict, flag), (patter_not_allow_update, False))


if __name__ == '__main__':
    unittest.main()