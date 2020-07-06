from game_number_based import GameNumberBased
from game_pattern_based import GamePatternBased
from input_output import take_input_for_pattern_game, display_message, option_to_quit, \
    take_input_for_number_game
from template import GAME_CONDITION, DRAW, TURN, UPDATE_MESSAGE, RESULT_MESSAGE, \
    GAME_DESCRIPTION

# player based on game
PLAYER_TYPE = {1: ["X", "O"],
               2: ["ODD", "EVEN"]}

# game based on condition
GAME_TYPE = {1: GamePatternBased,
             2: GameNumberBased}

# game mode
GAME_MODE = {'S', 'T'}


class Game(object):

    def __init__(self, game_type, player_mode, game_class):
        self._game_type = game_type
        self._player_mode = player_mode
        self._game_class = game_class
        self._player_flag = "X" if int(game_type) == 1 else "ODD"

    def get_player(self):
        """

        :return:
        """
        return self._player_flag

    def set_player(self, player):
        """

        :param player:
        :return:
        """
        self._player_flag = player

    def switch_player(self):
        """
         switch the player
        :return:
        """
        # get the player details based on game type
        player_dict = PLAYER_TYPE.get(int(self._game_type))
        self.set_player(player_dict[1] if self.get_player() == player_dict[0] else player_dict[0])

    def start_the_game(self):
        """

        :return:
        """
        # game_call
        game_object = self._game_class(self._player_mode)

        while True:
            # display the board
            game_object.board_view()

            # check for draw condition is any empty place existing
            if not game_object.is_empty_poisiton():
                display_message(DRAW)
                return

            display_message(TURN.format(self.get_player()))

            if int(self._game_type) == 1:
                # pattern based
                _x, _y, continue_flag = take_input_for_pattern_game(self._player_flag, player_mode, game_object)
                if not continue_flag:
                    return
                board_dict, update_flat = self._game_class.update_board_dict(int(_x), int(_y), self._player_flag,
                                                                             game_object.board_dict)
            else:
                _x, _y, _value, continue_flag = take_input_for_number_game(self._player_flag, player_mode, game_object)
                if not continue_flag:
                    return
                board_dict, update_flat = self._game_class.update_board_dict(int(_x), int(_y), _value,
                                                                             game_object.board_dict)

            # condition to check any one trying to update the existing value
            if not update_flat:
                display_message(UPDATE_MESSAGE)
                continue

            # game condition calls
            result, continue_flag = game_object.based_win_condition()
            display_message(RESULT_MESSAGE.format(result.format(self._player_flag)))

            # continue_flag is used to check is the player have won the game
            if not continue_flag:
                return

            # switch the player
            self.switch_player()


if __name__ == "__main__":
    game_type, player_mode = input(GAME_DESCRIPTION).split(",")
    game_class = GAME_TYPE.get(int(game_type), None)
    player_mode = player_mode.upper()
    if not (game_class and player_mode in GAME_MODE):
        display_message(GAME_CONDITION)
    else:
        game = Game(game_type, player_mode, game_class)
        game.start_the_game()
