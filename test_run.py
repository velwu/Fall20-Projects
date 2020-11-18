import argparse
import json

import mechanics
import print_board
import chess.svg
# Test 1. Get a Gardner board
# chess_board = mechanics.create_chess_board("Gardner")
# Test 2. Get a Jacobs–Meirovitz board
# chess_board = mechanics.create_chess_board("Jacobs–Meirovitz")
# Test 3. Get a Mallett board
# chess_board = mechanics.create_chess_board("Mallett")

# Test 4. Place some derelict pieces to test piece movement mechanics
location = (4,2)
chess_board = [[".", ".", ".", ".", "."] for i in range(5)]
mechanics.add_piece_forcibly(chess_board, 'r', location)

other_location = (2,0)
mechanics.add_piece_forcibly(chess_board, 'Q', other_location)
yet_other_location = (1,2)
mechanics.add_piece_forcibly(chess_board, "P", yet_other_location)
another_location_0 = (2,2)
mechanics.add_piece_forcibly(chess_board, "n", another_location_0)
another_location_1 = (4,0)
mechanics.add_piece_forcibly(chess_board, "k", another_location_1)
another_location_2 = (3,3)
mechanics.add_piece_forcibly(chess_board, 'B', another_location_2)
another_location_3 = (4,1)
mechanics.add_piece_forcibly(chess_board, "q", another_location_3)
another_location_4 = (1,0)
mechanics.add_piece_forcibly(chess_board, "P", another_location_4)
another_location_5 = (0,4)
mechanics.add_piece_forcibly(chess_board, "K", another_location_5)
another_location_6 = (3,0)
mechanics.add_piece_forcibly(chess_board, "P", another_location_6)


# According to the type of piece adjust function
print_board.print_board(chess_board, True)
piece_to_test = mechanics.get_piece_at_position(another_location_0,chess_board)
location_to_test = another_location_0
if (piece_to_test[0] in ['Q', 'q']):
    possible_moves = mechanics.get_queen_moves(location_to_test, chess_board)

elif (piece_to_test[0] in ['K', 'k']):
    possible_moves = mechanics.get_king_moves(location_to_test, chess_board)

elif (piece_to_test[0] in ['B', 'b']):
    possible_moves = mechanics.get_bishop_moves(location_to_test, chess_board)

elif (piece_to_test[0] in ['N', 'n']):
    possible_moves = mechanics.get_knight_moves(location_to_test, chess_board)

elif (piece_to_test[0] in ['R', 'r']):
    possible_moves = mechanics.get_rook_moves(location_to_test, chess_board)

print(json.dumps({"piece":piece_to_test,
                  str(len(possible_moves)) + " possible moves from current_location": location_to_test}))

"""
elif (piece == "knight"):
    print(json.dumps({"piece":piece,
                      "current_location": location,
                      "moves": mechanics.getKnightMoves(location, chess_board)}))


"""