from pieces import Position, Bishop, Rook, King, Queen, Knight, Pawn
from rich import print
class Board:
    """Represents a chess board with rook and bishop."""

    FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    RANKS = [1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, white_piece, black_piece, white_pos, black_pos):
        """
        Initialize the board with piece positions.

        Args:
            white_position (Position): Starting position of white piece
            black_position (Position): Starting position of the black piece
        """
        # Parse string positions to Position objects
        white_position = self.parse_position(white_pos)
        black_position = self.parse_position(black_pos)

        # White piece instantiation
        if white_piece == 'rook':
            self.white_piece = Rook(white_position, 'white')
        elif white_piece == 'bishop':
            self.white_piece = Bishop(white_position, 'white')
        elif white_piece == 'king':
            self.white_piece = King(white_position, 'white')
        elif white_piece == 'queen':
            self.white_piece = Queen(white_position, 'white')
        elif white_piece == 'knight':
            self.white_piece = Knight(white_position, 'white')
        elif white_piece == 'pawn':
            self.white_piece = Pawn(white_position, 'white')

        # Black piece instantiation
        if black_piece == 'rook':
            self.black_piece = Rook(black_position, 'black')
        elif black_piece == 'bishop':
            self.black_piece = Bishop(black_position, 'black')
        elif black_piece == 'king':
            self.black_piece = King(black_position, 'black')
        elif black_piece == 'queen':
            self.black_piece = Queen(black_position, 'black')
        elif black_piece == 'knight':
            self.black_piece = Knight(black_position, 'black')
        elif black_piece == 'pawn':
            self.black_piece = Pawn(black_position, 'black')

    def is_black_captured(self):
        """
        Check if the white piece can capture the black piece.

        Returns:
            bool: True if white can capture black
        """
        return self.white_piece.can_capture(self.black_piece.position)

    def is_white_captured(self):
        """
        Check if the black piece can capture the white piece.

        Returns:
            bool: True if black can capture white
        """
        return self.black_piece.can_capture(self.white_piece.position)

    def move_black(self, direction1, direction2, squares):
        """
        Move the black piece in the specified direction by the given number of squares.
        Handles wrapping around the board edges.

        Args:
            direction1 (str): 'up' or 'right'
            direction2 (str): 'left' or 'right'
            squares (int): Number of squares to move

        Returns:
            Position: New position of the black piece
        """
        current_file = self.black_piece.position.file
        current_rank = self.black_piece.position.rank

        file_index = self.FILES.index(current_file)
        rank_index = self.RANKS.index(current_rank)

        if self.black_piece.name == 'rook':
            if direction1 == 'up':
                # Move up (increase rank), wrap around if necessary                
                new_rank_index = (rank_index + squares) % len(self.RANKS)
                new_rank = self.RANKS[new_rank_index]
                
                new_position = Position(current_file, new_rank)
            elif direction1 == 'right':
                # Move right (increase file), wrap around if necessary
                new_file_index = (file_index + squares) % len(self.FILES)
                new_file = self.FILES[new_file_index]
                
                new_position = Position(new_file, current_rank)
            else:
                raise ValueError(f"Invalid direction: {direction1}")

        elif self.black_piece.name == 'bishop':
            if direction1 == 'up': # Diagonally up is up and to the right
                # Move up diagonally (increase rank and decrease file), wrap around if necessary
                new_rank_index = (rank_index + squares) % len(self.RANKS)
                new_file_index = (file_index + squares) % len(self.FILES)
                
                new_rank = self.RANKS[new_rank_index]
                new_file = self.FILES[new_file_index]
                
                new_position = Position(new_file, new_rank)
            elif direction1 == 'right': # Diagonally right is down and to the right
                # Move right diagonally (increase file and increase rank), wrap around if necessary
                new_rank_index = (rank_index - squares) % len(self.RANKS)
                new_file_index = (file_index + squares) % len(self.FILES)
                
                new_rank = self.RANKS[new_rank_index]
                new_file = self.FILES[new_file_index]
                
                new_position = Position(new_file, new_rank)
            else:
                raise ValueError(f"Invalid direction: {direction1}")

        elif self.black_piece.name == 'king':
            squares = 1 if squares >= 1 else 0 # King can only move 1 square
            if direction2 == 'straight':
                if direction1 == 'up':
                    # Move up (increase rank), wrap around if necessary
                    new_rank_index = (rank_index + squares) % len(self.RANKS)
                    new_rank = self.RANKS[new_rank_index]

                    new_position = Position(current_file, new_rank)
                elif direction1 == 'right':
                    # Move right (increase file), wrap around if necessary
                    new_file_index = (file_index + squares) % len(self.FILES)
                    new_file = self.FILES[new_file_index]

                    new_position = Position(new_file, current_rank)
                else:
                    raise ValueError(f"Invalid direction: {direction1}")
            elif direction2 == 'diagonal':
                # Move right diagonally (increase file and increase rank), wrap around if necessary
                if direction1 == 'up': # Diagonally up is up and to the right
                    # Move up diagonally (increase rank and decrease file), wrap around if necessary
                    new_rank_index = (rank_index + squares) % len(self.RANKS)
                    new_file_index = (file_index + squares) % len(self.FILES)
                    
                    new_rank = self.RANKS[new_rank_index]
                    new_file = self.FILES[new_file_index]
                    
                    new_position = Position(new_file, new_rank)
                elif direction1 == 'right': # Diagonally right is down and to the right
                    # Move right diagonally (increase file and increase rank), wrap around if necessary
                    new_rank_index = (rank_index - squares) % len(self.RANKS)
                    new_file_index = (file_index + squares) % len(self.FILES)
                    
                    new_rank = self.RANKS[new_rank_index]
                    new_file = self.FILES[new_file_index]
                    
                    new_position = Position(new_file, new_rank)
                else:
                    raise ValueError(f"Invalid direction: {direction1}")
            else:
                raise ValueError(f"Invalid direction: {direction2}")
            
        elif self.black_piece.name == 'queen':
            if direction2 == 'straight':
                if direction1 == 'up':
                    # Move up (increase rank), wrap around if necessary
                    new_rank_index = (rank_index + squares) % len(self.RANKS)
                    new_rank = self.RANKS[new_rank_index]

                    new_position = Position(current_file, new_rank)
                elif direction1 == 'right':
                    # Move right (increase file), wrap around if necessary
                    new_file_index = (file_index + squares) % len(self.FILES)
                    new_file = self.FILES[new_file_index]

                    new_position = Position(new_file, current_rank)
                else:
                    raise ValueError(f"Invalid direction: {direction1}")
            elif direction2 == 'diagonal':
                # Move right diagonally, wrap around if necessary
                if direction1 == 'up': # Diagonally up is up and to the right
                    # Move up diagonally (increase rank and decrease file), wrap around if necessary
                    new_rank_index = (rank_index + squares) % len(self.RANKS)
                    new_file_index = (file_index + squares) % len(self.FILES)
                    
                    new_rank = self.RANKS[new_rank_index]
                    new_file = self.FILES[new_file_index]
                    
                    new_position = Position(new_file, new_rank)
                elif direction1 == 'right': # Diagonally right is down and to the right
                    # Move right diagonally (increase file and increase rank), wrap around if necessary
                    new_rank_index = (rank_index - squares) % len(self.RANKS)
                    new_file_index = (file_index + squares) % len(self.FILES)
                    
                    new_rank = self.RANKS[new_rank_index]
                    new_file = self.FILES[new_file_index]
                    
                    new_position = Position(new_file, new_rank)
                else:
                    raise ValueError(f"Invalid direction: {direction1}")
            else:
                raise ValueError(f"Invalid direction: {direction2}")

        elif self.black_piece.name == 'knight':
            squares = 1 if squares >= 3 else 0 # Knight has to move as long as dice is >= 3
            if direction2 == 'straight':
                if direction1 == 'up':
                    # Move up and to the left (increase rank decrease file), wrap around if necessary
                    new_rank_index = (rank_index + squares * 2) % len(self.RANKS)
                    new_file_index = (file_index - squares * 1) % len(self.FILES)

                    new_rank = self.RANKS[new_rank_index]
                    new_file = self.FILES[new_file_index]

                    new_position = Position(new_file, new_rank)
                elif direction1 == 'right':
                    # Move right and up (increase rank increase file), wrap around if necessary
                    new_rank_index = (rank_index + squares * 2) % len(self.RANKS)
                    new_file_index = (file_index + squares * 1) % len(self.FILES)

                    new_rank = self.RANKS[new_rank_index]
                    new_file = self.FILES[new_file_index]

                    new_position = Position(new_file, new_rank)
                else:
                    raise ValueError(f"Invalid direction: {direction1}")
            elif direction2 == 'diagonal':
                # Move right diagonally (increase file and increase rank), wrap around if necessary
                if direction1 == 'up': # Diagonally up is up and to the right
                    # Move up diagonally (increase rank and increase file), wrap around if necessary
                    new_rank_index = (rank_index + squares * 1) % len(self.RANKS)
                    new_file_index = (file_index + squares * 2) % len(self.FILES)

                    new_rank = self.RANKS[new_rank_index]
                    new_file = self.FILES[new_file_index]
                    
                    new_position = Position(new_file, new_rank)
                elif direction1 == 'right': # Diagonally right is down and to the right
                    # Move right diagonally (increase file and increase rank), wrap around if necessary
                    new_rank_index = (rank_index - squares * 2) % len(self.RANKS)
                    new_file_index = (file_index + squares * 1) % len(self.FILES)

                    new_rank = self.RANKS[new_rank_index]
                    new_file = self.FILES[new_file_index]

                    new_position = Position(new_file, new_rank)
                else:
                    raise ValueError(f"Invalid direction: {direction1}")
        
        elif self.black_piece.name == 'pawn':
            # Pawn can only move in one direction for one space
            if squares >= 1:
                new_rank_index = (rank_index - 1) % len(self.RANKS)

                new_rank = self.RANKS[new_rank_index]

                new_position = Position(current_file, new_rank)
            else:
                new_position = Position(current_file, current_rank)

        self.black_piece.move_to(new_position)
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
            rank_even = True if rank % 2 else False
            self.board_str += f"{rank} "
            for j, file in enumerate(self.FILES, 1):
                file_even = True if j % 2 else False
                piece_on_square = None
                # Checks for square bracket color and uses ANSI for color output
                if rank_even:
                    if file_even:
                        left_bracket, right_bracket = "\033[90m" + "[" + "\033[0m", "\033[90m" + "]" + "\033[0m"
                    else:
                        left_bracket, right_bracket = "\033[97m" + "[" + "\033[0m", "\033[97m" + "]" + "\033[0m"
                else:
                    if file_even:
                        left_bracket, right_bracket = "\033[97m" + "[" + "\033[0m", "\033[97m" + "]" + "\033[0m"
                    else:
                        left_bracket, right_bracket = "\033[90m" + "[" + "\033[0m", "\033[90m" + "]" + "\033[0m"

                if self.white_piece.position.rank == rank and self.white_piece.position.file == file:
                    if self.white_piece.name == 'king':
                        piece_on_square = "\033[97m" + 'Ḵ' + "\033[0m"
                    else:
                        piece_on_square = "\033[97m" + self.white_piece.name[0].upper() + "\033[0m"
                elif self.black_piece.position.rank == rank and self.black_piece.position.file == file:
                    if self.black_piece.name == 'king':
                        piece_on_square = "\033[90m" + 'Ḵ' + "\033[0m"
                    else:
                        piece_on_square = "\033[90m" + self.black_piece.name[0].upper() + "\033[0m"

                if piece_on_square:
                    self.board_str += f"{left_bracket}{piece_on_square}{right_bracket}"
                else:
                    self.board_str += left_bracket + " " + right_bracket
            if rank != 1:
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
