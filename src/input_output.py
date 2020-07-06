from template import PATTERN_GAME_MESSAGE, NUMBER_GAME_MESSAGE, \
    QUIT_MESSAGE, QUIT_CHECK_MESSAGE, ODD_NUMBER_ALLOWED, EVEN_NUMBER_ALLOWED


def option_to_quit():
    """

    used to quit the game
    :return:
    """
    _cont = input(QUIT_MESSAGE)
    if _cont.upper() == "Y":
        return True
    else:
        display_message(QUIT_CHECK_MESSAGE)
        return False


def take_input_for_pattern_game(player, game_mode, game_object):
    """

    :return:
    """
    # pattern based came input
    try:
        # pattern based came input
        if player == 'O' and game_mode == 'S':
            _x, _y = game_object.get_computer_move()
        else:
            _x, _y = map(int, input(PATTERN_GAME_MESSAGE).split(","))
        return _x, _y, True
    except:
        if option_to_quit():
            return None, None, False
        else:
            return take_input_for_pattern_game(player, game_mode, game_object)


def take_input_for_number_game(player, game_mode, game_object):
    """

    :return:
    """
    try:
        # number based came input
        if player == 'EVEN' and game_mode == 'S':
            _x, _y, _value = game_object.get_computer_move()
        else:
            _x, _y, _value = map(int, input(NUMBER_GAME_MESSAGE).split(","))

        # use for checking that player can't input different values
        if player == "ODD" and not _value % 2 == 1:
            display_message(ODD_NUMBER_ALLOWED)
            return take_input_for_number_game(player, game_mode, game_object)

        if player == "EVEN" and not _value % 2 == 0:
            display_message(EVEN_NUMBER_ALLOWED)
            return take_input_for_number_game(player, game_mode, game_object)

        return _x, _y, _value, True
    except:
        if option_to_quit():
            return None, None, None, False
        else:
            return take_input_for_number_game(player, game_mode, game_object)




def display_message(message):
    """

    :param message:
    :return:
    """
    print(message)



