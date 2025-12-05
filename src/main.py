"""
Rook vs Bishop Chess Game
A simulation where a rook tries to survive 15 rounds without being captured by a bishop.

The rook moves based on:
- Coin flip: Heads = move up, Tails = move right
- Dice roll: Sum of two 6-sided dice determines number of squares to move
- Wrapping: Board wraps around at edges (toroidal topology)

The bishop remains stationary at c3.
The rook starts at h1.
"""

from game import ChessMiniGame
import argparse
import random

def main():
    """Run the Rook vs Bishop game."""
    # Initialize the game with default settings
    # Bishop at input/random square (stationary), Rook at input/random square (moving), Rounds at input/15
    parser = argparse.ArgumentParser(
        description="Piece vs. Piece game simulation"
    )

    parser.add_argument(
        '--white',
        default='bishop c3',
        help='Bishop starting piece and position (default: c3)'
    )
    parser.add_argument(
        '--black',
        default='rook h1',
        help='Rook starting piece and position (default: h1)'
    )
    parser.add_argument(
        '--rounds',
        default='15',
        help='Number of rounds to play'
    )
    parser.add_argument(
        '--seed',
        default='',
        help='Seed fo game to be generated'
    )
    args = parser.parse_args()

    if args.seed:
        random.seed(int(args.seed))

    valid_pieces = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
    valid_rank = ['1', '2', '3', '4', '5', '6', '7', '8']
    valid_file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    
    white_idx_space = args.white.lower().index(" ")
    black_idx_space = args.black.lower().index(" ")

    if (not args.white[:white_idx_space] in valid_pieces or
        not args.white[white_idx_space+1:white_idx_space+2] in valid_file or
        not args.white[white_idx_space+2:white_idx_space+3] in valid_rank):
        raise Exception("White piece not a valid piece or rank or file not valid")
    if (not args.black[:black_idx_space] in valid_pieces or
        not args.black[black_idx_space+1:black_idx_space+2] in valid_file or
        not args.black[black_idx_space+2:black_idx_space+3] in valid_rank):
        raise Exception("Black piece not a valid piece or rank or file not valid")

    white_split = args.white.split(" ")
    black_split = args.black.split(" ")

    if (not white_split[0] in valid_pieces or
        not white_split[1][0] in valid_file or
        not white_split[1][1] in valid_rank):
        raise Exception("White piece not a valid piece or rank or file not valid")
    if (not black_split[0] in valid_pieces or
        not black_split[1][0] in valid_file or
        not black_split[1][1] in valid_rank):
        raise Exception("Black piece not a valid piece or rank or file not valid")

    game = ChessMiniGame(
        white_piece=white_split[0],
        black_piece=black_split[0],
        white_pos=white_split[1],
        black_pos=black_split[1],
        rounds=args.rounds
    )

    # Play the game
    winner = game.play()

    # Display final result
    final_msg = f"FINAL WINNER: {winner.upper()}"
    print(f"\n{'*' * len(final_msg)}")
    print(final_msg)
    print(f"{'*' * len(final_msg)}\n")


if __name__ == "__main__":
    main()