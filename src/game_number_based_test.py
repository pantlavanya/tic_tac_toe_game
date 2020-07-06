from unittest import TestCase
import unittest
from game_number_based import GameNumberBased


# patter based game
number_game_winner_ODD_row = {(0,0): 1, (1,0): 2, (0,1): 5, (2,1): 8, (0,2): 9}
number_game_winner_ODD_column = {(0,1): 1, (1,0): 2, (2,1): 5, (2,0): 8, (1,1): 9}
number_game_winner_ODD_diagonal = {(0,0): 1, (1,0): 2, (1,1): 5, (2,0): 8, (2,2): 9}

number_game_winner_EVEN_row = {(0,0): 3, (0,1): 4, (1,0): 5, (0,2): 8}
number_game_winner_EVEN_column = {(0,0): 3, (0,1): 4, (1,0): 5, (0,2): 8}
number_game_winner_EVEN_diagonal = {(0,0): 3, (1,1): 4, (1,0): 5, (2,2): 8}

number_game_winner_draw = {(0,0): 1, (0,1): 3, (0,2): 2, (1,0): 4, (1,1): 5,
                            (1,2): 6, (2,0): 7, (2,1): 9, (2,2): 8}

number_game_continue = {(0,0): 1, (2,2): 2}

number_not_allow_update = {(0,0): 1, (0,1): 2}


class TicTacToeGameTestCase(TestCase):

    def setUp(self):
        self.game_object = GameNumberBased('T')

    def run_test(self, given_answer, expected_out):
        """

        :param given_answer:
        :param expected_out:
        :return:
        """
        self.assertEqual(given_answer, expected_out)

    def test_winner_ODD_row(self):
        """

        test case to check ODD is the winner for patter_game_winner_ODD_row input
        :return:
        """
        self.game_object.board_dict = number_game_winner_ODD_row
        result, _ = self.game_object.based_win_condition()
        self.run_test((result.format("ODD"), _), ('Won (The player ODD has met the criteria for win)', False))

    def test_winner_ODD_column(self):
        """

        test case to check ODD is the winner for test_winner_ODD_column input
        :return:
        """
        self.game_object.board_dict = number_game_winner_ODD_column
        result, _ = self.game_object.based_win_condition()
        self.run_test((result.format("ODD"), _), ('Won (The player ODD has met the criteria for win)', False))

    def test_winner_ODD_diagonal(self):
        """

        test case to check ODD is the winner for test_winner_ODD_diagonal input
        :return:
        """
        self.game_object.board_dict = number_game_winner_ODD_diagonal
        result, _ = self.game_object.based_win_condition()
        self.run_test((result.format("ODD"), _), ('Won (The player ODD has met the criteria for win)', False))

    def test_winner_EVEN_row(self):
        """

        test case to check EVEN is the winner for test_winner_EVEN_row input
        :return:
        """
        self.game_object.board_dict = number_game_winner_EVEN_row
        result, _ = self.game_object.based_win_condition()
        self.run_test((result.format("EVEN"), _), ('Won (The player EVEN has met the criteria for win)', False))

    def test_winner_EVEN_column(self):
        """

        test case to check EVEN is the winner for test_winner_EVEN_column input
        :return:
        """
        self.game_object.board_dict = number_game_winner_EVEN_column
        result, _ = self.game_object.based_win_condition()
        self.run_test((result.format("EVEN"), _), ('Won (The player EVEN has met the criteria for win)', False))

    def test_winner_EVEN_diagonal(self):
        """

        test case to check EVEN is the winner for test_winner_EVEN_diagonal input
        :return:
        """
        self.game_object.board_dict = number_game_winner_EVEN_diagonal
        result, _ = self.game_object.based_win_condition()
        self.run_test((result.format("EVEN"), _), ('Won (The player EVEN has met the criteria for win)', False))

    def test_patter_game_draw(self):
        """

        test case to check the game is draw
        :return:
        """
        self.game_object.board_dict = number_game_winner_draw
        empty_block = self.game_object.is_empty_poisiton()
        self.run_test(empty_block, 0)

    def test_patter_game_continue(self):
        """

        test case to check the game will continue
        :return:
        """
        self.game_object.board_dict = number_game_continue
        result, _ = self.game_object.based_win_condition()
        self.run_test((result, _), ("Continue (The game should continue)", True))

    def test_patter_game_update_existing(self):
        """

        test case to check we can't update existing
        :return:
        """
        board_dict, flag = GameNumberBased.update_board_dict(0, 1, 'ODD', number_not_allow_update)
        self.run_test((board_dict, flag), (number_not_allow_update, False))


if __name__ == '__main__':
    unittest.main()