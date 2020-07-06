import copy, random
from operator import itemgetter
from game_common_feature import GameCommonFeature
from template import WON_MESSAGE, CONTINUE_MESSAGE


class GameNumberBased(GameCommonFeature):

    @staticmethod
    def number_win_condition_check(board_dict):
        """

        use to check condition winning
        :param board_dict:
        :return:
        """
        # get point with same x point
        for i in range(0, 3):
            # row combination
            row_comb = list(board_dict[(_x,_y)] for _x, _y in board_dict.keys() if _x == i)
            # col combination
            col_comb = list(board_dict[(_x, _y)] for _x, _y in board_dict.keys() if _y == i)

            if all(row_comb) and sum(row_comb) == 15:
                return True

            if all(col_comb) and sum(col_comb) == 15:
                return True

        if all([board_dict.get((0, 0), None), board_dict.get((1, 1), None), board_dict.get((2, 2), None)]) and \
                        sum(itemgetter(*[(0, 0), (1, 1), (2, 2)])(board_dict)) == 15:
            return True

        if all([board_dict.get((0, 2), None), board_dict.get((1, 1), None), board_dict.get((2, 0), None)]) and \
                        sum(itemgetter(*[(0, 2), (1, 1), (2, 0)])(board_dict)) == 15:
            return True

        return False

    def based_win_condition(self):
        """

        :return:
        """
        point_check = self.number_win_condition_check(self.board_dict)
        if point_check:
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
                for _value in [2,4,6,8]:
                    if not board_copy[(i, j)]:
                        board_copy, update_flag = GameNumberBased.update_board_dict(i, i, _value, board_copy)
                        point_check = GameNumberBased.number_win_condition_check(board_copy)
                        if point_check:
                            return i, j, _value

        # Check if the player could win on his next move, and block them.
        for i in range(0, 3):
            for j in range(0, 3):
                board_copy = copy.deepcopy(self.board_dict)
                for _value in [1,3,5,7,9]:
                    if not board_copy[(i, j)]:
                        board_copy, update_flag = GameNumberBased.update_board_dict(i, j, _value, board_copy)
                        point_check = GameNumberBased.number_win_condition_check(board_copy)
                        if point_check:
                            return i, j, random.choice(set([2,4,6,8]) - set(board_copy.values()))

        # take one of the corners
        move = self.computer_next_move([(0, 0), (0, 2), (2, 0), (2, 2)])
        if move:
            return move

        # take the center
        if not self.board_dict[(1, 1)]:
            return 1, 1, random.choice(list(set([2,4,6,8]) - set(board_copy.values())))

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
            _x, _y = random.choice(available_moves)
            return _x, _y, random.choice(list(set([2,4,6,8]) - set(self.board_dict.values())))
        return None

