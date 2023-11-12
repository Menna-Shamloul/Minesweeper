import random
# create a board to represent the minesweeper game
class Board:
    def __init__(self, dim_size, num_bombs):
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

    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for  r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # if r and c are the same as location that we are checking continue
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs
    
    def dig(self, row, col):
        # dig at that location, return true if successful dig, false if bomb dug
        self.dug.add((row, col)) # track that we dug here

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        # self.board[row][col]==0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        return True

    def __str__(self):
        # self string displays the current minesweeper board situation
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # create a new array which the user will see
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )




# play the game
def play(dim_size=10, num_bombs=10):
    # create the board and plant the bombs
    board = Board(dim_size, num_bombs)