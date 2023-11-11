import random
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
    
    def make_new_board(self):
        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*' # plant the bomb
            bombs_planted += 1
        
        return board
    
    def assign_values_to_board(self):
        # assign number for all empty spaces which represents how many neighboring bombs there are
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)


# play the game
def play(dim_size=10, num_bombs=10):