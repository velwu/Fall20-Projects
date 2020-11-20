import chess
#import sunfish
import math
import random
import pandas as pd
import sys
import chess.svg
import mechanics

def print_board(board_class, is_list_bool):
    uni_pieces = {'r':' ♜ ', 'n':' ♞ ', 'b':' ♝ ', 'q':' ♛ ', 'k':' ♚ ', 'p':' ♟ ',
                  'R':' ♖ ', 'N':' ♘ ', 'B':' ♗ ', 'Q':' ♕ ', 'K':' ♔ ', 'P':' ♙ ', '.':' 口 '}

    #print(board_test)
    if is_list_bool:
        board_obj = []
        for each_row in board_class:
            single_row_list = (pd.Series(each_row)).map(uni_pieces)
            single_row_str = ''.join(list(single_row_list))
            board_obj.append(single_row_str)
            # board_obj.insert(0, list(single_row_list))
        print(*board_obj, sep="\n")

    else:
        board_obj = str(board_class)
        for key in uni_pieces.keys():
            board_obj = board_obj.replace(key, uni_pieces[key])
        print(board_obj)

def print_game_tree(test_chess_board, which_player):
    print("Original board:")
    print_board(test_chess_board, True)
    print("\n")

    some_opening_boards_turn1 = mechanics.generate_game_tree(test_chess_board, which_player)

    for each_idx, each_opening in enumerate(some_opening_boards_turn1):
        print("Possible board No.", str(each_idx+1))
        print_board(each_opening, True)
        mechanics.check_for_winner(each_opening, 'k', 'K')
        print("\n")
    return some_opening_boards_turn1
