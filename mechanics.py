import argparse
import json
import chess
import print_board
import numpy as np
import copy

map_letter_reps_to_piece_names = {
    'R': 'Black Rook', 'N': 'Black Knight', 'B': 'Black Bishop',
    'Q': 'Black Queen', 'K': 'Black King', 'P': 'Black Pawn',
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
                    #print("Detecting an enemy", piece_at_new_pos[1], "at", new_pos)
                    solution_moves.append(new_pos)
                    break

                elif piece_at_new_pos[0].isupper() == this_rook[0].isupper():
                    #If it's an ally piece:
                    #print("Detecting an ally", piece_at_new_pos[1], "at", new_pos)
                    break
            else:
                break
    #print("All possible moves with this Rook:", solution_moves)
    return solution_moves

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
                    #print("Detecting an enemy", piece_at_new_pos[1], "at", new_pos)
                    solution_moves.append(new_pos)
                    break

                elif piece_at_new_pos[0].isupper() == this_bishop[0].isupper():
                    # If it's an ally piece:
                    #print("Detecting an ally", piece_at_new_pos[1], "at", new_pos)
                    break
            else:
                break
    #print("All possible moves with this Bishop:", solution_moves)
    return solution_moves

def get_knight_moves(current_pos, chess_board):
    solution_moves = []
    this_knight = get_piece_at_position(current_pos, chess_board)
    # Look for potential moves in all 8 possible moves
    knight_directions = [[1, 2], [1, -2], [-1, -2], [-1, 2],
                         [2, 1], [2, -1], [-2, -1], [-2, 1]]
    for each_direction in knight_directions:
        knight_current = list(current_pos)
        knight_current = np.add(knight_current, each_direction)
        new_pos = tuple(knight_current)
        if not on_chess_board(chess_board, new_pos):
            continue

        elif on_chess_board(chess_board, new_pos):
            piece_at_new_pos = get_piece_at_position(new_pos, chess_board)
            if piece_at_new_pos[0] == ".":
                solution_moves.append(new_pos)

            elif piece_at_new_pos[0].isupper() != this_knight[0].isupper():
                # If it's an enemy piece
                #print("Detecting an enemy", piece_at_new_pos[1], "at", new_pos)
                solution_moves.append(new_pos)
                continue

            elif piece_at_new_pos[0].isupper() == this_knight[0].isupper():
                # If it's an ally piece:
                #print("Detecting an ally", piece_at_new_pos[1], "at", new_pos)
                continue
            else:
                continue
    #print("All possible moves with this Knight:", solution_moves)
    return solution_moves

def get_queen_moves(current_pos, chess_board):
    solution_moves = []
    this_queen = get_piece_at_position(current_pos, chess_board)
    # Look for potential moves in all 8 directions: Vertical, Horizontal and Diagonal ones
    queen_directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                        [1, 1], [1, -1], [-1, -1], [-1, 1]]
    for each_direction in queen_directions:
        # print("Trying direction:", each_direction)
        queen_current = list(current_pos)
        while True:
            queen_current = np.add(queen_current, each_direction)
            new_pos = tuple(queen_current)
            if not on_chess_board(chess_board, new_pos):
                break

            elif on_chess_board(chess_board, new_pos):
                piece_at_new_pos = get_piece_at_position(new_pos, chess_board)
                if piece_at_new_pos[0] == ".":
                    solution_moves.append(new_pos)

                elif piece_at_new_pos[0].isupper() != this_queen[0].isupper():
                    # If it's an enemy piece
                    #print("Detecting an enemy", piece_at_new_pos[1], "at", new_pos)
                    solution_moves.append(new_pos)
                    break

                elif piece_at_new_pos[0].isupper() == this_queen[0].isupper():
                    # If it's an ally piece:
                    #print("Detecting an ally", piece_at_new_pos[1], "at", new_pos)
                    break
            else:
                break
    #print("All possible moves with this Queen:", solution_moves)
    return solution_moves

def get_king_moves(current_pos, chess_board):
    solution_moves = []
    this_king = get_piece_at_position(current_pos, chess_board)
    # Look for potential moves in all 8 possible moves
    king_directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                        [1, 1], [1, -1], [-1, -1], [-1, 1]]
    for each_direction in king_directions:
        king_current = list(current_pos)
        king_current = np.add(king_current, each_direction)
        new_pos = tuple(king_current)
        if not on_chess_board(chess_board, new_pos):
            continue

        elif on_chess_board(chess_board, new_pos):
            piece_at_new_pos = get_piece_at_position(new_pos, chess_board)
            if piece_at_new_pos[0] == ".":
                solution_moves.append(new_pos)

            elif piece_at_new_pos[0].isupper() != this_king[0].isupper():
                # If it's an enemy piece
                # print("Detecting an enemy", piece_at_new_pos[1], "at", new_pos)
                solution_moves.append(new_pos)
                continue

            elif piece_at_new_pos[0].isupper() == this_king[0].isupper():
                # If it's an ally piece:
                # print("Detecting an ally", piece_at_new_pos[1], "at", new_pos)
                continue
            else:
                continue
    #print("All possible moves with this King:", solution_moves)
    return solution_moves

#TODO: Get Pawn moves
def get_pawn_moves(current_pos, chess_board):
    solution_moves = []
    this_pawn = get_piece_at_position(current_pos, chess_board)
    # The first moves in these lists are regular moves, whereas the other two are attacking moves
    pawn_directions_top_player = [[1,0], [1, 1], [1, -1]]
    pawn_directions_bot_player = [[-1,0], [-1, 1], [-1, -1]]

    if this_pawn[0].isupper() == True:
        pawn_directions = pawn_directions_top_player
    else:
        pawn_directions = pawn_directions_bot_player

    # Check the regular move first
    pawn_current = list(current_pos)
    pawn_current = np.add(pawn_current, pawn_directions[0])
    new_pos = tuple(pawn_current)
    # Regular move only works if it is within board boundaries and detects an empty square
    if on_chess_board(chess_board, new_pos) and get_piece_at_position(new_pos, chess_board)[0] == ".":
        solution_moves.append(new_pos)

    # Then check the 2 attack moves

    for each_attack_move in pawn_directions[1:]:
        pawn_current = list(current_pos)
        pawn_current = np.add(pawn_current, each_attack_move)
        new_pos = tuple(pawn_current)
        if not on_chess_board(chess_board, new_pos):
            continue
        piece_at_new_pos = get_piece_at_position(new_pos, chess_board)
        if piece_at_new_pos[0].isupper() != this_pawn[0].isupper() and piece_at_new_pos[0] != ".":
            # Only add to this Pawn's moves if it's an enemy piece
            solution_moves.append(new_pos)
    #print("All possible moves with this Pawn:", solution_moves)
    return solution_moves

def generate_game_tree(chess_board, current_player):
    #TODO: This function currently only works for 1 round.
    # Expand it so it can walk through the whole game

    all_new_boards = list()

    if current_player == "White":
        queen_to_move = 'q'
        king_to_move = 'k'
        bishop_to_move = 'b'
        knight_to_move = 'n'
        rook_to_move = 'r'
        pawn_to_move = 'p'
    elif current_player == "Black":
        queen_to_move = 'Q'
        king_to_move = 'K'
        bishop_to_move = 'B'
        knight_to_move = 'N'
        rook_to_move = 'R'
        pawn_to_move = 'P'
    else:
        print("Current player format ERROR. Check input!!")
        return None

    for each_row_idx, each_row_val in enumerate(chess_board):
        for each_square_idx, each_square_val in enumerate(each_row_val):
            location_to_test = (each_row_idx, each_square_idx)
            if (each_square_val == queen_to_move):
                possible_moves = get_queen_moves(location_to_test, chess_board)

            elif (each_square_val == king_to_move):
                possible_moves = get_king_moves(location_to_test, chess_board)

            elif (each_square_val == bishop_to_move):
                possible_moves = get_bishop_moves(location_to_test, chess_board)

            elif (each_square_val == knight_to_move):
                possible_moves = get_knight_moves(location_to_test, chess_board)

            elif (each_square_val == rook_to_move):
                possible_moves = get_rook_moves(location_to_test, chess_board)

            elif (each_square_val == pawn_to_move):
                possible_moves = get_pawn_moves(location_to_test, chess_board)
            else:
                #print("There is no movable piece in that square:", location_to_test)
                continue

            for each_possible_move in possible_moves:
                new_chess_board = copy.deepcopy(chess_board)
                all_new_boards.append(move_piece_by_set_pos(location_to_test, each_possible_move,
                                      new_chess_board, each_square_val))

    return all_new_boards



#TODO: Play the whole game (no AI, but generate exhaustive game tree)
#TODO: Write the analysis
#TODO: Start small. Try some 3*3 boards which are mostly solved (with any piece combinations, perhaps??)

