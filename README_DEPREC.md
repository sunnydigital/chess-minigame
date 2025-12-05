# rook-vs-bishop
Repository for the Zus Health take-home Rook vs. Bishop assignment

Under the understanding that no extraneous packages need to be installed, will be continuing with the code

# Design Process (Notes)
An object-oriented approach was taken to designing the pieces, board, game, then main function to run everything

Noted from the diagram that the Rook is black and the Bishop is white

Added argument parsing to specify seed and initial starting position

Created a custom UI to represent the pieces on the board, displaying the Rook and Bishop with color as well as the board
    - Tried a few different UI elements, from emoji pieces to emoji checkerboards, none aligned well

Utilized custom classes to print colored pieces and board

Integrating all pieces: for pieces such as King, Queen, and Knight with multiple axis movement will roll two die

AI was used in initial idea generation, syntax queries, parts of refactoring repetitive code, debugging, and parts of README generation. This was done in consideration of an exploration vs exploitation standpoint, personal learning vs. task performance