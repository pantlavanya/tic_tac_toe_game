import copy, random
from utils import update_board_dict, is_empty_poisiton


def get_all_keys_for_x_and_o(board_dict):
    """

    get all keys for both players
    :param board_dict:
    :return:
    """
    x_keys = list(key for key in board_dict if 'X' == board_dict[key])
    y_keys = list(key for key in board_dict if 'O' == board_dict[key])
    return x_keys, y_keys


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


def patter_based_win_condition(board_dict):
    """

    :param board_dict:
    :return:
    """
    x_keys, y_keys = get_all_keys_for_x_and_o(board_dict)
    if len(x_keys) > 2 or len(y_keys) > 2:
        x_point_check = win_condition_check(x_keys)
        if x_point_check:
            return "Won (The player {0} has met the criteria for win)", False
        y_point_check = win_condition_check(y_keys)
        if y_point_check:
            return "Won (The player {0} has met the criteria for win)", False

    return "Continue (The game should continue)", True


def get_computer_move(board_dict, player_value):
    """

    :param board:
    :param computerLetter:
    :return:
    """
    # check if computer can win in the next move
    for i in range(0, 3):
        for j in range(0, 3):
            board_copy = copy.deepcopy(board_dict)
            if not board_dict[(i, j)]:
                update_board_dict(i, j, player_value, board_copy)
                _, result_flag = patter_based_win_condition(board_copy, player_value)
                if not result_flag:
                    return i

    # Check if the player could win on his next move, and block them.
    next_player = 'X'
    for i in range(0, 3):
        for j in range(0, 3):
            board_copy = copy.deepcopy(board_dict)
            if not board_dict[(i, j)]:
                update_board_dict(i, j, next_player, board_copy)
                _, result_flag = patter_based_win_condition(board_copy, player_value)
                if not result_flag:
                    return i

    # Try to take one of the corners, if they are free.
    move = computer_next_move(board_dict, [(0, 0), (0, 2), (2, 0), (2, 2)])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if not board_dict[(1, 1)]:
        return 5

    # Move on one of the sides.
    return computer_next_move(board_dict, [(0,1), (1,0), (1, 2), (2, 1)])


def computer_next_move(board_dict, movesList):
    """

    :param board:
    :param movesList:
    :return:
    """

    possibleMoves = []
    for i in movesList:
        if not board_dict[(i, j)]:
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
