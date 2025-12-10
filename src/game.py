import random
from board import Board


class ChessMiniGame:
    """Simulates the Rook vs Bishop survival game."""

    def __init__(self, white_piece='bishop', black_piece='rook', white_pos='c3', black_pos='h1', rounds=15):
        """
        Initialize the game.

        Args:
            white_piece (str): Piece name of white (default: 'bishop')
            black_piece (str): Piece name of black (default: 'rook')
            white_pos (str): Starting position of white (default: 'c3')
            black_pos (str): Starting position of black (default: 'h1')
            rounds (int): Number of rounds to play (default: 15)
        """
        self.board = Board(
            white_piece = white_piece,
            black_piece = black_piece,
            white_pos = white_pos,
            black_pos = black_pos
        )
        self.rounds = int(rounds)
        self.current_round = 0

    def flip_coin(self):
        """
        Flip a coin to determine direction.

        Returns:
            str: 'heads' or 'tails'
        """
        return random.choice(['heads', 'tails'])

    def roll_dice(self):
        """
        Roll two 6-sided dice.

        Returns:
            tuple: (die1, die2, total)
        """
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        return die1, die2, total

    def play_round(self):
        """
        Play a single round of the game.

        Returns:
            bool: True if rook was captured, False otherwise
        """
        self.current_round += 1

        round_msg = f"ROUND {self.current_round}"
        print(f"\n{'=' * len(round_msg)}")
        print(round_msg)
        print(f"{'=' * len(round_msg)}")

        # Step 1: Flip two coins for direction
        # Check if the piece is valid for a linear combination of two directions using two coin tosses
        coin1 = self.flip_coin()
        coin2 = self.flip_coin()
        direction1 = 'up' if coin1 == 'heads' else 'right'

        lin_combo_pieces = ['king', 'queen', 'knight']
        direction2 = None

        if self.board.black_piece.name in lin_combo_pieces:
            direction2 = 'straight' if coin2 == 'heads' else 'diagonal' # Uses a combination of two movement sets limited to the top right quadrant to decide movements for Queen, King, Knight
            print(f"Coin toss 1: {coin1.upper()} Coin toss 2: {coin2.upper()} -> Moving {direction2} and to the {direction1}")
        else:
            print(f"Coin toss: {coin1.upper()} -> Moving {direction1}")

        # Step 2: Roll dice for distance
        die1, die2, total = self.roll_dice()
        print(f"Dice roll: {die1} + {die2} = {total} squares")

        # Step 3: Move the black piece
        print(f"Black position before move: {self.board.black_piece.position}")
        new_position = self.board.move_black(direction1, direction2, total)
        print(f"Black position after move: {new_position}")
    
        # Step 4: Display the board
        print(self.board.display_board())

        # Step 5: Check if rook was captured
        if self.board.is_black_captured():
            capture_msg = f"BLACK {self.board.black_piece.name.upper()} CAPTURED! White {self.board.white_piece.name.capitalize()} can capture the Black {self.board.black_piece.name.capitalize()} at this position!"
            print("\n" + "!" * len(capture_msg))
            print(capture_msg)
            print("!" * len(capture_msg))
            return True

        print(f"\nBlack {self.board.black_piece.name.capitalize()} is safe this round.")
        return False

    def play(self):
        """
        Play the full game for the specified number of rounds.

        Returns:
            str: 'white' if white wins, 'black' if black wins
        """
        title_msg = f"{self.board.white_piece.name.upper()} VS {self.board.black_piece.name.upper()}"
        print("\n" + "*" * len(title_msg))
        print(title_msg)
        print("*" * len(title_msg))
        print(f"\nStarting positions:")
        print(f"  {self.board.white_piece.name.capitalize()} (White): {self.board.white_piece.position} (stationary)")
        print(f"  {self.board.black_piece.name.capitalize()} (Black): {self.board.black_piece.position} (starting position)")
        print(f"\nThe {self.board.black_piece.name.capitalize()} must survive {self.rounds} rounds to win!")

        for _ in range(self.rounds):
            captured = self.play_round()
            if captured:
                win_msg = f"GAME OVER - WHITE {self.board.white_piece.name.upper()} WINS!"
                print("\n" + "=" * len(win_msg))
                print(win_msg)
                print("=" * len(win_msg))
                print(f"The Black {self.board.black_piece.name.capitalize()} was captured in round {self.current_round}.")
                return 'white'

        win_msg = f"GAME OVER - BLACK {self.board.black_piece.name.upper()} WINS!"
        print("\n" + "=" * len(win_msg))
        print(win_msg)
        print("=" * len(win_msg))
        print(f"The Black {self.board.black_piece.name.capitalize()} survived all {self.rounds} rounds!")
        return 'black'
