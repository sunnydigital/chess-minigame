from pieces import Position, Bishop, Rook


class Board:
    """Represents a chess board with rook and bishop."""

    FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    RANKS = [1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, bishop_position, rook_position):
        """
        Initialize the board with piece positions.

        Args:
            bishop_position (Position): Starting position of the bishop
            rook_position (Position): Starting position of the rook
        """
        self.bishop = Bishop(bishop_position)
        self.rook = Rook(rook_position)

    def is_rook_captured(self):
        """
        Check if the bishop can capture the rook.

        Returns:
            bool: True if bishop can capture rook
        """
        return self.bishop.can_capture(self.rook.position)

    def is_bishop_captured(self):
        """
        Check if the rook can capture the bishop.

        Returns:
            bool: True if rook can capture bishop
        """
        return self.rook.can_capture(self.bishop.position)

    def move_rook(self, direction, squares):
        """
        Move the rook in the specified direction by the given number of squares.
        Handles wrapping around the board edges.

        Args:
            direction (str): 'up' or 'right'
            squares (int): Number of squares to move

        Returns:
            Position: New position of the rook
        """
        current_file = self.rook.position.file
        current_rank = self.rook.position.rank

        if direction == 'up':
            # Move up (increase rank), wrap around if necessary
            file_index = self.FILES.index(current_file)
            new_rank_index = (self.RANKS.index(current_rank) + squares) % len(self.RANKS)
            new_rank = self.RANKS[new_rank_index]
            new_position = Position(current_file, new_rank)
        elif direction == 'right':
            # Move right (increase file), wrap around if necessary
            file_index = self.FILES.index(current_file)
            new_file_index = (file_index + squares) % len(self.FILES)
            new_file = self.FILES[new_file_index]
            new_position = Position(new_file, current_rank)
        else:
            raise ValueError(f"Invalid direction: {direction}")

        self.rook.move_to(new_position)
        return new_position

    def display_board(self):
        """
        Output a visual display of the board with the positions of the rook and bishop.
        Args:
            rook (Rook): The rook piece
            bishop (Bishop): The bishop piece

        Returns:
            str: Visual/string representation of the board
        """
        self.board_str = ""

        # Output the files from a to h
        self.board_str = "   " + "  ".join(self.FILES) + "\n"

        for rank in self.RANKS[::-1]: # Ranks are reversed top to bottom: 8 -> 1
            self.board_str += f"{rank} "
            for file in self.FILES:
                piece_on_square = None # Sanity check
                if self.bishop.position.rank == rank and self.bishop.position.file == file:
                    piece_on_square = "B"
                elif self.rook.position.rank == rank and self.rook.position.file == file:
                    piece_on_square = "R"
                
                if piece_on_square:
                    self.board_str += f"[{piece_on_square}]"
                else:
                    self.board_str += "[ ]"
            self.board_str += "\n"

        return self.board_str

    @staticmethod
    def parse_position(position_str):
        """
        Parse a position string like 'c3' into a Position object.

        Args:
            position_str (str): Position string (e.g., 'c3')

        Returns:
            Position: Position object
        """
        file = position_str[0]
        rank = int(position_str[1])
        return Position(file, rank)
