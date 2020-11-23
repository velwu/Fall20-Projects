import argparse
import json
import chess
import print_board
import numpy as np
import copy
import random
import time

map_letter_reps_to_piece_names = {
    'R': 'White Rook', 'N': 'White Knight', 'B': 'White Bishop',
    'Q': 'White Queen', 'K': 'White King', 'P': 'White Pawn',
    'r': 'Black Rook', 'n': 'Black Knight', 'b': 'Black Bishop',
    'q': 'Black Queen', 'k': 'Black King', 'p': 'Black Pawn',
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
        chess_board[0] = ['r', 'n', 'b', 'q', 'k']
        chess_board[1] = ['p' for p in range(5)]
        chess_board[-2] = ['P' for p in range(5)]
        chess_board[-1] = ['R', 'N', 'B', 'Q', 'K']

    elif variant_name == "Jacobs–Meirovitz":
        chess_board[0] = ['b', 'n', 'r', 'q', 'k']
        chess_board[1] = ['p' for p in range(5)]
        chess_board[-2] = ['P' for p in range(5)]
        chess_board[-1] = ['K', 'Q', 'R', 'N', 'B']

    elif variant_name == "Mallett":
        chess_board[0] = ['r', 'b', 'q', 'k', 'b']
        chess_board[1] = ['p' for p in range(5)]
        chess_board[-2] = ['P' for p in range(5)]
        chess_board[-1] = ['R', 'N', 'Q', 'K', 'N']

    elif variant_name == "THOC":
        chess_board = [[".", ".", "."] for i in range(4)]
        chess_board[0] = ['n', 'b', 'r']
        chess_board[1] = ['p', ".", "."]
        chess_board[-2] = [".", ".", "P"]
        chess_board[-1] = ["R", "B", "N"]

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

def get_pawn_moves(current_pos, chess_board):
    solution_moves = []
    this_pawn = get_piece_at_position(current_pos, chess_board)
    # The first moves in these lists are regular moves, whereas the other two are attacking moves
    pawn_directions_top_player = [[1,0], [1, 1], [1, -1]]
    pawn_directions_bot_player = [[-1,0], [-1, 1], [-1, -1]]

    if this_pawn[0].isupper() == True:
        # If the char is capitalized, then it represents a White pieces
        pawn_directions = pawn_directions_bot_player
    else:
        # Else, a de-capitalized char represents a Black piece
        pawn_directions = pawn_directions_top_player

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
        queen_to_move = 'Q'
        king_to_move = 'K'
        bishop_to_move = 'B'
        knight_to_move = 'N'
        rook_to_move = 'R'
        pawn_to_move = 'P'
    elif current_player == "Black":
        queen_to_move = 'q'
        king_to_move = 'k'
        bishop_to_move = 'b'
        knight_to_move = 'n'
        rook_to_move = 'r'
        pawn_to_move = 'p'
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

def check_for_winner(chess_board, white_essential_piece, black_essential_piece):
    # Usually white_essential_piece == "White King (k)" and black_essential_piece == "Black King (K)"
    # But in my mind, I have some ideas for custom games where Queen or Bishop substitutes King as essential
    # So i just left the essential pieces as parameters in case I need them
    if not any(white_essential_piece in sublist for sublist in chess_board):
        print("Black has won.")
        return "Black"
    elif not any(black_essential_piece in sublist for sublist in chess_board):
        print("White has won.")
        return "White"
    else:
        print("The game goes on")
        return None

#TODO: Play the whole game (no AI, but generate exhaustive game tree) with elimination rules
def play_a_game_of_elimination(variant_name):
    initial_chess_board = create_chess_board(variant_name)
    # chess_board_status_str = ''.join(map(str,chess_board))

    print("The game begins.")
    print_board.print_board(initial_chess_board, True)

    while True:
        print("It is now White's turn")
        time.sleep(2)
        list_of_next_boards = generate_game_tree(initial_chess_board, "White")
        board_after_white_plays = random.choice(list_of_next_boards)
        chess_board_status_str = ''.join(map(str, board_after_white_plays))
        if chess_board_status_str.isupper():
            print("All Black pieces eliminated. The White Player has won.")
            final_board = board_after_white_plays
            break
        print_board.print_board(board_after_white_plays, True)
        print("It is now Black's turn")
        time.sleep(2)
        list_of_next_boards = generate_game_tree(board_after_white_plays, "Black")
        board_after_black_plays = random.choice(list_of_next_boards)
        chess_board_status_str = ''.join(map(str, board_after_black_plays))
        if chess_board_status_str.islower():
            print("All White pieces eliminated. The Black Player has won.")
            final_board = board_after_black_plays
            break
        print_board.print_board(board_after_black_plays, True)
        initial_chess_board = board_after_black_plays
        continue

    print("The game is over.")
    print_board.print_board(final_board, True)
    return final_board

#TODO: Write a func which detects checks for whether either sides' essential (King in default settings)
# is under attack and cut out the tree branch if a move cannot remove that threat
def detect_check(chess_board, white_essential_piece, black_essential_piece):

    return

#TODO: What about stalemate(s) though???
def detect_stalemate(chess_board):
    return

#TODO: Play the whole game (no AI, but generate exhaustive game tree) with standard King-slaying rules

#TODO: Downsize the analysis to probably 3x4, with only some select pieces
#TODO: Start small. Try some 3*3 boards which are mostly solved (with any piece combinations, perhaps??)

#TODO: Write the analysis


