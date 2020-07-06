from operator import itemgetter


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


def number_based_win_condition(board_dict):
    """

    :param board_dict:
    :return:
    """
    point_check = number_win_condition_check(board_dict)
    if point_check:
        return "Won (The player {0} has met the criteria for win)", False
    return "Continue (The game should continue)", True
