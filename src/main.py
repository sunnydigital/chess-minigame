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

from game import RookVsBishopGame
import argparse
import random

def main():
    """Run the Rook vs Bishop game."""
    # Initialize the game with default settings
    # Bishop at input/random square (stationary), Rook at input/random square (moving), Rounds at input/15
    parser = argparse.ArgumentParser(
        description="Rook vs. Bishop game simulation"
    )

    parser.add_argument(
        '--bishop',
        default='c3',
        help='Bishop starting position (default: c3)'
    )
    parser.add_argument(
        '--rook',
        default='h1',
        help='Rook starting position (default: h1)'
    )
    parser.add_argument(
        '--rounds',
        default='15',
        help='Number of rounds to play'
    )
    parser.add_argument(
        '--seed',
        default='123',
        help='Seed fo game to be generated'
    )
    args = parser.parse_args()

    if args.seed:
        random.seed(int(args.seed))

    game = RookVsBishopGame(
        bishop_pos=args.bishop, 
        rook_pos=args.rook, 
        rounds=args.rounds)

    # Play the game
    winner = game.play()

    # Display final result
    print(f"\n{'*'*60}")
    print(f"FINAL WINNER: {winner.upper()}")
    print(f"{'*'*60}\n")


if __name__ == "__main__":
    main()