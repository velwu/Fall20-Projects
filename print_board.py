import chess
#import sunfish
import math
import random
import pandas as pd
import sys
import chess.svg

def print_board(board_class, is_list_bool):
    uni_pieces = {'r':' ♜ ', 'n':' ♞ ', 'b':' ♝ ', 'q':' ♛ ', 'k':' ♚ ', 'p':' ♟ ',
                  'R':' ♖ ', 'N':' ♘ ', 'B':' ♗ ', 'Q':' ♕ ', 'K':' ♔ ', 'P':' ♙ ', '.':' 口 '}

    #print(board_test)
    if is_list_bool:
        board_obj = []
        for each_row in board_class:
            single_row_list = (pd.Series(each_row)).map(uni_pieces)
            board_obj.append(list(single_row_list))
            # board_obj.insert(0, list(single_row_list))
        print(*board_obj, sep="\n")

    else:
        board_obj = str(board_class)
        for key in uni_pieces.keys():
            board_obj = board_obj.replace(key, uni_pieces[key])
        print(board_obj)