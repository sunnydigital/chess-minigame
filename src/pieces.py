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

    def __init__(self, position: Position, color: str):
        """
        Initialize a chess piece.

        Args:
            position (Position): Starting position
            color (str): 'white' or 'black'
        """
        self.position = position
        self.color = color

    def move_to(self, new_position: Position):
        """Move the piece to a new position."""
        self.position = new_position


class Bishop(Piece):
    """Bishop chess piece - moves diagonally."""

    def __init__(self, position, color):
        """Initialize a bishop."""
        super().__init__(position, color)
        self.name = 'bishop'

    def can_capture(self, target_position: Position):
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
        return file_diff == rank_diff and self.position != target_position


class Rook(Piece):
    """Rook chess piece - moves horizontally or vertically."""

    def __init__(self, position: Position, color):
        """Initialize a black rook."""
        super().__init__(position, color)
        self.name = 'rook'

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

class King(Piece):
    """King chess piece - moves horizontally, vertically, or diagonally one square"""

    def __init__(self, position, color):
        """Initializa a king"""
        super().__init__(position, color)
        self.name = 'king'

    def can_capture(self, target_position):
        """
        Check if the king can capture a piece at the target position.
        King moves horizontally, vertically, or diagonally for one square.

        Args:
            target_position (Position): Position to check

        Returns:
            bool: True if king can capture at target position
        """
        # King can capture if on same file (vertical) or same rank (horizontal) or on a diagonal which is one space away
        file_diff = abs(ord(self.position.file) - ord(target_position.file))
        rank_diff = abs(self.position.rank - target_position.rank)
        
        one_diff = True if file_diff == 1 or rank_diff == 1 else False

        same_file = self.position.file == target_position.file 
        same_rank = self.position.rank == target_position.rank
        
        return one_diff and (((same_file or same_rank) or (file_diff == rank_diff)) and self.position != target_position)

class Queen(Piece):
    """Queen chess piece - moves horizontally, vertically, or diagonally"""

    def __init__(self, position, color):
        """Initializa a queen"""
        super().__init__(position, color)
        self.name = 'queen'

    def can_capture(self, target_position):
        """
        Check if the queen can capture a piece at the target position.
        Queen moves horizontally, vertically, or diagonally.

        Args:
            target_position (Position): Position to check

        Returns:
            bool: True if queen can capture at target position
        """
        # Queen can capture if on same file (vertical) or same rank (horizontal) or on a diagonal
        file_diff = abs(ord(self.position.file) - ord(target_position.file))
        rank_diff = abs(self.position.rank - target_position.rank)

        same_file = self.position.file == target_position.file 
        same_rank = self.position.rank == target_position.rank
        
        return (((same_file or same_rank) or (file_diff == rank_diff)) and self.position != target_position)

class Knight(Piece):
    """Knight chess piece - moves horizontally, vertically, or diagonally"""

    def __init__(self, position, color):
        """Initializa a knight"""
        super().__init__(position, color)
        self.name = 'knight'

    def can_capture(self, target_position):
        """
        Check if the knight can capture a piece at the target position.
        Knight moves horizontally, vertically, or diagonally.

        Args:
            target_position (Position): Position to check

        Returns:
            bool: True if knight can capture at target position
        """
        # Knight can capture if 3 squares away on same file (vertical) or same rank (horizontal) and one square away on the other rank/file
        file_diff = abs(ord(self.position.file) - ord(target_position.file))
        rank_diff = abs(self.position.rank - target_position.rank)
        
        return ((file_diff == 2 and rank_diff == 1) or (file_diff == 1 and rank_diff == 2)) and self.position != target_position

class Pawn(Piece):
    """Pawn chess piece - moves horizontally, vertically, or diagonally"""

    def __init__(self, position, color):
        """Initializa a pawn"""
        super().__init__(position, color)
        self.name = 'pawn'

    def can_capture(self, target_position):
        """
        Check if the pawn can capture a piece at the target position.
        Pawn moves horizontally, vertically, or diagonally.

        Args:
            target_position (Position): Position to check

        Returns:
            bool: True if pawn can capture at target position
        """
        # Pawn can capture if on diagonal files/ranks one space apart facing the direction of travel: white captures up black captures down
        file_diff = abs(ord(self.position.file) - ord(target_position.file))
        rank_diff = self.position.rank - target_position.rank # Directionally aware rank
        
        if self.color == 'white':
            if file_diff == 1 and rank_diff == -1: # Needs target to be diagonally adjacent above
                return True
        if self.color == 'black':
            if file_diff == 1 and rank_diff == 1: # Needs target to be diagonally adjacent below
                return True
        return False