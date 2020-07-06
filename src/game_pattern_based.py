import copy, random
from game_common_feature import GameCommonFeature
from template import WON_MESSAGE, CONTINUE_MESSAGE


class GamePatternBased(GameCommonFeature):

    @staticmethod
    def get_all_keys_for_x_and_o(board_dict):
        """

        get all keys for both players
        :param board_dict:
        :return:
        """
        x_keys = list(key for key in board_dict if 'X' == board_dict[key])
        y_keys = list(key for key in board_dict if 'O' == board_dict[key])
        return x_keys, y_keys

    @staticmethod
    def win_condition_check(x_keys):
        """

        :param x_keys:
        :return:
        """
        # check
        # get point with same x point
        for i in range(0, 3):
            # row combination
            row_comb = list(True for _x, _y in x_keys if _x == i)
            # col combination
            col_comb = list(True for _x, _y in x_keys if _y == i)
            if len(row_comb) == 3 or len(col_comb) == 3:
                return True

        if (0, 0) in x_keys and (1, 1) in x_keys and (2, 2) in x_keys:
            return True

        if (0, 2) in x_keys and (1, 1) in x_keys and (2, 0) in x_keys:
            return True

        return False

    def based_win_condition(self):
        """

        :param board_dict:
        :return:
        """
        x_keys, y_keys = GamePatternBased.get_all_keys_for_x_and_o(self.board_dict)
        if len(x_keys) > 2 or len(y_keys) > 2:
            x_point_check = GamePatternBased.win_condition_check(x_keys)
            if x_point_check:
                return WON_MESSAGE, False
            y_point_check = GamePatternBased.win_condition_check(y_keys)
            if y_point_check:
                return WON_MESSAGE, False

        return CONTINUE_MESSAGE, True

    def get_computer_move(self):
        """

        :param board:
        :param computerLetter:
        :return:
        """
        # check if computer can win in the next move
        for i in range(0, 3):
            for j in range(0, 3):
                board_copy = copy.deepcopy(self.board_dict)
                if not board_copy[(i, j)]:
                    board_copy, update_flag = GamePatternBased.update_board_dict(i, j, 'O', board_copy)
                    x_keys, y_keys = GamePatternBased.get_all_keys_for_x_and_o(board_copy)
                    y_point_check = GamePatternBased.win_condition_check(y_keys)
                    if y_point_check:
                        return i, j

        # Check if the player could win on his next move, and block them.
        for i in range(0, 3):
            for j in range(0, 3):
                board_copy = copy.deepcopy(self.board_dict)
                if not board_copy[(i, j)]:
                    board_copy, update_flag = GamePatternBased.update_board_dict(i, j, 'X', board_copy)
                    x_keys, y_keys = GamePatternBased.get_all_keys_for_x_and_o(board_copy)
                    x_point_check = GamePatternBased.win_condition_check(x_keys)
                    if x_point_check:
                        return i, j

        # take one of the corners
        move = self.computer_next_move([(0, 0), (0, 2), (2, 0), (2, 2)])
        if move:
            return move

        # take the center
        if not self.board_dict[(1, 1)]:
            return 1, 1

        # any remaining position
        return self.computer_next_move([(0,1), (1,0), (1, 2), (2, 1)])

    def computer_next_move(self, move_list):
        """

        :param move_list:
        :return:
        """

        available_moves = []
        for i, j in move_list:
            if not self.board_dict[(i, j)]:
                available_moves.append((i, j))
        if len(available_moves) > 0:
            return random.choice(available_moves)
        return None
