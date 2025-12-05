import random
from board import Board


class RookVsBishopGame:
    """Simulates the Rook vs Bishop survival game."""

    def __init__(self, bishop_pos='c3', rook_pos='h1', rounds=15):
        """
        Initialize the game.

        Args:
            bishop_pos (str): Starting position of bishop (default: 'c3')
            rook_pos (str): Starting position of rook (default: 'h1')
            rounds (int): Number of rounds to play (default: 15)
        """
        self.board = Board(
            Board.parse_position(bishop_pos),
            Board.parse_position(rook_pos)
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

        print(f"\n{'='*60}")
        print(f"ROUND {self.current_round}")
        print(f"{'='*60}")

        # Step 1: Flip coin for direction
        coin = self.flip_coin()
        direction = 'up' if coin == 'heads' else 'right'
        print(f"Coin toss: {coin.upper()} -> Moving {direction}")

        # Step 2: Roll dice for distance
        die1, die2, total = self.roll_dice()
        print(f"Dice roll: {die1} + {die2} = {total} squares")

        # Step 3: Move the rook
        print(f"Rook position before move: {self.board.rook.position}")
        new_position = self.board.move_rook(direction, total)
        print(f"Rook position after move: {new_position}")
    
        # Step 4: Display the board
        print(self.board.display_board())

        # Step 5: Check if rook was captured
        if self.board.is_rook_captured():
            print("\n" + "!"*60)
            print("ROOK CAPTURED! Bishop can capture the rook at this position!")
            print("!"*60)
            return True

        print("\n" + "Rook is safe this round.")
        return False

    def play(self):
        """
        Play the full game for the specified number of rounds.

        Returns:
            str: 'bishop' if bishop wins, 'rook' if rook wins
        """
        print("\n" + "*"*60)
        print("ROOK VS BISHOP")
        print("*"*60)
        print(f"\nStarting positions:")
        print(f"  Bishop (White): {self.board.bishop.position} (stationary)")
        print(f"  Rook (Black): {self.board.rook.position} (starting position)")
        print(f"\nThe rook must survive {self.rounds} rounds to win!")

        for _ in range(self.rounds):
            captured = self.play_round()
            if captured:
                print("\n" + "="*60)
                print("GAME OVER - BISHOP WINS!")
                print("="*60)
                print(f"The rook was captured in round {self.current_round}.")
                return 'bishop'

        print("\n" + "="*60)
        print("GAME OVER - ROOK WINS!")
        print("="*60)
        print(f"The rook survived all {self.rounds} rounds!")
        return 'rook'
