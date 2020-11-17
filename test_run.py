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
location = (2,2)
chess_board = [[".", ".", ".", ".", "."] for i in range(5)]
mechanics.add_piece_forcibly(chess_board, 'r', location)

other_location = (2,0)
mechanics.add_piece_forcibly(chess_board, 'Q', other_location)
yet_other_location = (2,1)
mechanics.add_piece_forcibly(chess_board, "P", yet_other_location)
another_location = (3,2)
mechanics.add_piece_forcibly(chess_board, "n", another_location)

print_board.print_board(chess_board, True)

# According to the type of piece adjust function
piece = mechanics.get_piece_at_position(location,chess_board)
if (piece[0] in ['R', 'r']):
    possible_moves = mechanics.get_rook_moves(location, chess_board)
    print(json.dumps({"piece":piece,
                      "current_location": location,
                      str(len(possible_moves)) + " possible moves": len(possible_moves)}))

"""
elif (piece == "knight"):
    print(json.dumps({"piece":piece,
                      "current_location": location,
                      "moves": mechanics.getKnightMoves(location, chess_board)}))


"""