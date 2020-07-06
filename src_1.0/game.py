from game_pattern_based import patter_based_win_condition, get_computer_move
from game_number_based import number_based_win_condition
from utils import create_board_dict, board_view, update_board_dict, is_empty_poisiton,\
    option_to_quit


# game based on condition
GAME_TYPE = {1: patter_based_win_condition,
             2: number_based_win_condition}

# player based on game
PLAYER_TYPE = {1: ["X", "O"],
               2: ["ODD", "EVEN"]}


def start_the_game(g_type, player_mode):
    """

    :param g_type: g_type can be 1 or 2
    :param player_mode: g_type can be S or M
    :return:
    """
    # create the dict of the board
    board_dict = create_board_dict()
    # get the function as per the game type
    game_call = GAME_TYPE.get(int(g_type), None)
    if not game_call:
        print("game only have 2 type either x_o(1) or number(2)")
        return

    # get the player details based on game type
    player_dict = PLAYER_TYPE.get(int(g_type))
    # player name
    flag = PLAYER_TYPE.get(int(g_type))[0]
    while True:
        # display the board
        board_view(board_dict)
        # check for draw condition is any empty place existing
        if not is_empty_poisiton(board_dict):
            print("\n\t\tDraw (No more positions available)\n")
            return

        print("\n\t{0}'s turn".format(flag))

        if int(g_type) == 1:
            try:
                # pattern based came input
                _x, _y = map(int, input("""\t\tenter the position (x,y) \n
                                           Enter Xpoint,Ypoint comma seperated \n
                                           Example :- 0,1 \n""").split(","))
            except:
                if option_to_quit():
                    return
                else:
                    continue

        else:
            try:
                # number based came input
                _x, _y, _value = map(int, input("""\t\tenter the position (x,y, value) \n
                                                    Enter Xpoint,Ypoint,value comma seperated \n
                                                    Example :- 0,1,2 \n""").split(","))
            except:
                if option_to_quit():
                    return
                else:
                    continue

            # use for checking that player can't input different values
            if flag == "ODD" and not _value % 2 == 1:
                print("\n\t ODD player input number allowed are [1,3,5,7,9]\n")
                continue
            if flag == "EVEN" and not _value % 2:
                print("\n\t EVEN player input number allowed are [2,4,6,8]\n")
                continue

            board_dict, update_flat = update_board_dict(int(_x), int(_y), _value, board_dict)

        # condition to check any one trying to update the existing value
        import pdb;pdb.set_trace()
        if not update_flat:
            print ("\n\t cant update existing value, please try again\n")
            continue

        # game condition calls
        result, continue_flag = game_call(board_dict)
        print("\n\t\t{0}\n".format(result.format(flag)))

        # continue_flag is used to check is the player have won the game
        if not continue_flag:
            return

        # switch the player
        flag = player_dict[1] if flag == player_dict[0] else player_dict[0]


if __name__ == "__main__":
    game_type, player_mode = input("""\n\n\t\tWe have 2 type of games pattern(X, O) or number(even, odd)\n
                                       Enter 1 for Pattern (x, o) based game\n
                                       Enter 2 for Number (odd, even) based game\n
                                       1st player will be X or odd always\n\n
                                       Enter S for Single Player\n
                                       Enter M for Multi Player\n""").split(",")
    start_the_game(game_type, player_mode)