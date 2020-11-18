import argparse
import json
import chess
import print_board
import numpy as np

map_letter_reps_to_piece_names = {
    'R': 'Black Rook', 'N': 'Black Knight', 'B': 'Black Bishop',
    'Q': 'Black Queen', 'K': 'Black King', 'P': 'BLack Pawn',
    'r': 'White Rook', 'n': 'White Knight', 'b': 'White Bishop',
    'q': 'White Queen', 'k': 'White King', 'p': 'White Pawn',
    '.': 'nothing'
}

def on_chess_board(chess_board, pos_tuple):
    if pos_tuple[0] < 0 or pos_tuple[1] < 0:
        return False
    try:
        chess_board[pos_tuple[0]][pos_tuple[1]]
    except (ValueError, IndexError):
        return False
    else:
        return True

def add_piece_forcibly(chess_board, piece_to_add, position_tuple):
    chess_board[position_tuple[0]][position_tuple[1]] = piece_to_add
    print("Adding a", map_letter_reps_to_piece_names[piece_to_add], "at", position_tuple)

    return chess_board

def move_piece_by_set_pos(current_position_tuple, movement_tuple, chess_board, piece_to_move):
    # current_position_tuple = (old_row, old_col)
    # movement_tuple = (move_row, move_col)
    chess_board[current_position_tuple[0]][current_position_tuple[1]] = "."
    chess_board[movement_tuple[0]][movement_tuple[1]] = piece_to_move

    return chess_board

def get_piece_at_position(pos, chess_board):
    # print("Position queried:", pos)
    the_one_piece = chess_board[pos[0]][pos[1]]

    piece_name = map_letter_reps_to_piece_names[the_one_piece]
    # print("The piece at", pos, "is a", map_letter_reps_to_piece_names[the_one_piece])
    return the_one_piece, piece_name

def create_chess_board(variant_name):

    chess_board = [[".", ".", ".", ".", "."] for i in range(5)]

    if variant_name == "Gardner":
        chess_board[0] = ['R', 'N', 'B', 'Q', 'K']
        chess_board[1] = ['P' for p in range(5)]
        chess_board[-2] = ['p' for p in range(5)]
        chess_board[-1] = ['r', 'n', 'b', 'q', 'k']

    if variant_name == "Jacobs–Meirovitz":
        chess_board[0] = ['B', 'N', 'R', 'Q', 'K']
        chess_board[1] = ['P' for p in range(5)]
        chess_board[-2] = ['p' for p in range(5)]
        chess_board[-1] = ['k', 'q', 'r', 'n', 'b']

    elif variant_name == "Mallett":
        chess_board[0] = ['R', 'B', 'Q', 'K', 'B']
        chess_board[1] = ['P' for p in range(5)]
        chess_board[-2] = ['p' for p in range(5)]
        chess_board[-1] = ['r', 'n', 'q', 'k', 'n']

    # print("Board type:", variant_name, "\n", *chess_board, sep="\n")
    print("Board type:", variant_name)

    return chess_board

def get_rook_moves(current_pos, chess_board):
    """ A function that returns the all possible moves of a Rook at a given position
        current_pos: The current position of the Rook, represented by a tuple
        chess_board: The current game board state represented by a 2D array/list
    """
    solution_moves = []
    this_rook = get_piece_at_position(current_pos, chess_board)
    # Look for potential moves in all 4 directions: 2 horizontal, 2 vertical
    rook_directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for each_direction in rook_directions:
        rook_current = list(current_pos)
        while True:
            rook_current = np.add(rook_current, each_direction)
            new_pos = tuple(rook_current)
            if not on_chess_board(chess_board, new_pos):
                # print("Going out of board")
                break

            elif on_chess_board(chess_board, new_pos):
                piece_at_new_pos = get_piece_at_position(new_pos, chess_board)
                if piece_at_new_pos[0] == ".":
                    solution_moves.append(new_pos)

                elif piece_at_new_pos[0].isupper() != this_rook[0].isupper():
                    # If it's an enemy piece
                    print("Detecting an enemy", piece_at_new_pos[1], "at", new_pos)
                    solution_moves.append(new_pos)
                    break

                elif piece_at_new_pos[0].isupper() == this_rook[0].isupper():
                    #If it's an ally piece:
                    print("Detecing an ally", piece_at_new_pos[1], "at", new_pos)
                    break
            else:
                break
    print("All possible moves with this Rook:", solution_moves)
    return solution_moves

#TODO: Get Bishop moves
def get_bishop_moves(current_pos, chess_board):
    """ A function that returns the all possible moves of a Rook at a given position
        current_pos: The current position of the Rook, represented by a tuple
        chess_board: The current game board state represented by a 2D array/list
    """
    solution_moves = []
    this_bishop = get_piece_at_position(current_pos, chess_board)
    # Look for potential moves in all 4 diagonal directions
    bishop_directions = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    for each_direction in bishop_directions:
        # print("Trying direction:", each_direction)
        bishop_current = list(current_pos)
        while True:
            bishop_current = np.add(bishop_current, each_direction)
            new_pos = tuple(bishop_current)
            if not on_chess_board(chess_board, new_pos):
                break

            elif on_chess_board(chess_board, new_pos):
                piece_at_new_pos = get_piece_at_position(new_pos, chess_board)
                if piece_at_new_pos[0] == ".":
                    solution_moves.append(new_pos)

                elif piece_at_new_pos[0].isupper() != this_bishop[0].isupper():
                    # If it's an enemy piece
                    print("Detecting an enemy", piece_at_new_pos[1], "at", new_pos)
                    solution_moves.append(new_pos)
                    break

                elif piece_at_new_pos[0].isupper() == this_bishop[0].isupper():
                    # If it's an ally piece:
                    print("Detecing an ally", piece_at_new_pos[1], "at", new_pos)
                    break
            else:
                break
    print("All possible moves with this Bishop:", solution_moves)
    return solution_moves

#TODO: Get Queen moves
#TODO: Get Knight moves
#TODO: Get King moves
#TODO: Get Pawn moves
#TODO: Play the whole game (no AI, but generate exhastive game tree)
#TODO: Write the analysis
#TODO: Start small. Try some 3*3 boards which are mostly solved (with any piece combinations, perhaps??)
"""
def getKnightMoves(pos, chess_board):

    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_alpha_to_index[column]
    i,j = row, column
    solution_moves = []
    try:
        temp = chess_board[i + 1][j - 2]
        solution_moves.append([i + 1, j - 2])
    except:
        pass
    try:
        temp = chess_board[i + 2][j - 1]
        solution_moves.append([i + 2, j - 1])
    except:
        pass
    try:
        temp = chess_board[i + 2][j + 1]
        solution_moves.append([i + 2, j + 1])
    except:
        pass
    try:
        temp = chess_board[i + 1][j + 2]
        solution_moves.append([i + 1, j + 2])
    except:
        pass
    try:
        temp = chess_board[i - 1][j + 2]
        solution_moves.append([i - 1, j + 2])
    except:
        pass
    try:
        temp = chess_board[i - 2][j + 1]
        solution_moves.append([i - 2, j + 1])
    except:
        pass
    try:
        temp = chess_board[i - 2][j - 1]
        solution_moves.append([i - 2, j - 1])
    except:
        pass
    try:
        temp = chess_board[i - 1][j - 2]
        solution_moves.append([i - 1, j - 2])
    except:
        pass

    # Filter all negative values
    temp = [i for i in solution_moves if i[0] >=0 and i[1] >=0]
    allPossibleMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in temp]
    allPossibleMoves.sort()
    return allPossibleMoves

"""


# TEST CODES below: Might delete later~

#test_board_1 = create_chess_board("Gardner")
#print_board.print_board(test_board_1, True)

#test_board_2 = create_chess_board("Mallett")
#print_board.print_board(test_board_2, True)
