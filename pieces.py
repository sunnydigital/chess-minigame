class Position:
    """Represents a position on the chess board."""

    def __init__(self, file, rank):
        """
        Initialize a position.

        Args:
            file (str): Column letter (a-h)
            rank (int): Row number (1-8)
        """
        self.file = file
        self.rank = rank

    def __eq__(self, other):
        """Check if two positions are equal."""
        if not isinstance(other, Position):
            return False
        return self.file == other.file and self.rank == other.rank

    def __str__(self):
        """String representation of position."""
        return f"{self.file}{self.rank}"

    def __repr__(self):
        """Debug representation of position."""
        return f"Position({self.file}, {self.rank})"


class Piece:
    """Base class for chess pieces."""

    def __init__(self, position, color):
        """
        Initialize a chess piece.

        Args:
            position (Position): Starting position
            color (str): 'white' or 'black'
        """
        self.position = position
        self.color = color

    def move_to(self, new_position):
        """Move the piece to a new position."""
        self.position = new_position


class Bishop(Piece):
    """Bishop chess piece - moves diagonally."""

    def __init__(self, position):
        """Initialize a white bishop."""
        super().__init__(position, 'white')

    def can_capture(self, target_position):
        """
        Check if the bishop can capture a piece at target position.
        Bishop moves diagonally in all 4 directions.

        Args:
            target_position (Position): Position to check

        Returns:
            bool: True if bishop can capture at target position
        """
        # Convert file letters to numbers for calculation
        file_diff = abs(ord(self.position.file) - ord(target_position.file))
        rank_diff = abs(self.position.rank - target_position.rank)

        # Bishop can capture if target is on a diagonal (file_diff == rank_diff)
        return file_diff == rank_diff and file_diff > 0


class Rook(Piece):
    """Rook chess piece - moves horizontally or vertically."""

    def __init__(self, position):
        """Initialize a black rook."""
        super().__init__(position, 'black')

    def can_capture(self, target_position):
        """
        Check if the rook can capture a piece at target position.
        Rook moves horizontally or vertically.

        Args:
            target_position (Position): Position to check

        Returns:
            bool: True if rook can capture at target position
        """
        # Rook can capture if on same file (vertical) or same rank (horizontal)
        same_file = self.position.file == target_position.file
        same_rank = self.position.rank == target_position.rank

        return (same_file or same_rank) and self.position != target_position