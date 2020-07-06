
board_keys = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
board_dict = {}


def create_board_dict():
    """

    create board dict
    :return:
    """
    for points in board_keys:
        board_dict[points] = None
    return board_dict


def board_view(board_dict):
    """

    used to display board
    :return:
    """
    for i in range(0,3):
        print ("  ", end='|')
        for j in range(0, 3):
            print("{0}".format( board_dict[(i,j)] if board_dict[(i,j)] else " "), end="|")
        print("\n-----------")


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
    if not exist_value:
        board_dict[(x, y)] = value
        flag = True
    return board_dict, flag


def is_empty_poisiton(board_dict):
    """

    check if the next position exist
    :return:
    """
    return len(list(filter(lambda x: x is None, board_dict.values())))


def option_to_quit():
    """

    used to quit the game
    :return:
    """
    _cont = input("""\t\tDo you want to quit ?\n
                     \t\tEnter Y to Quit or any other key to continue\n""")
    if _cont.upper() == "Y":
        return True
    else:
        print("Please enter Xpoint,Ypoint,value comma seperated")
        return False