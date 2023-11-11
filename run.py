# create a board to represent the minesweeper game
class Board:
    def _init_(self, dim_size, num_bombs):
        # track these parameters
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        # create the board
        self.board = self.make_new_board()
        # assign value to each cell class
        self.assign_values_to_board()
        # initialize a set to track which locations uncovered and save (row,col) tuples into this set
        self.dug = set()


# play the game
def play(dim_size=10, num_bombs=10):