from abc import ABC, abstractmethod


class GameCommonFeature(ABC):

    board_keys = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    def __init__(self, player_mode):
        """

        create board dict
        :return:
        """
        self.board_dict = {}
        for points in GameCommonFeature.board_keys:
            self.board_dict[points] = None
        self.player_mode = player_mode

    def board_view(self):
        """

        used to display board
        :return:
        """
        for i in range(0, 3):
            print("  ", end='|')
            for j in range(0, 3):
                print("{0}".format(self.board_dict[(i, j)] if self.board_dict[(i, j)] else " "), end="|")
            print("\n-----------")

    @staticmethod
    def update_board_dict(x, y, value, board_dict):
        """

        update the board value
        :param x:
        :param y:
        :param value:
        :return:
        """
        exist_value = board_dict.get((x, y), None)
        flag = False
        if not (value in ['X', 'O']) and value in board_dict.values():
            return board_dict, False
        if not exist_value:
            board_dict[(x, y)] = value
            flag = True
        return board_dict, flag

    def is_empty_poisiton(self):
        """

        check if the next position exist
        :return:
        """
        return len(list(filter(lambda x: x is None, self.board_dict.values())))

    @abstractmethod
    def based_win_condition(self):
        pass

    @abstractmethod
    def get_computer_move(self, player):
        pass


