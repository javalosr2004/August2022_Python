import random

class Board():
    def __init__(self, dim_size, num_bombs):
        #let's keep track of these paramaters
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #let's create the board
        #helper function
        self.board = self.make_new_board()

        #initialize a set to keep track of which locations we've uncovered
        #we'll save (row, col) tuples into this set
        self.dug = set() #if we dig at 0,0, then self.dug = (0, 0)

        #initialize 
    def make_new_board(self):
        #step 1. create the board and plant the bombs
        #step 2. show the user the board and ask for where they want to dig

        #generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        #plant the bombs
        bombs_planted = 0

        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                pass
            else:
                board[row][col] = '*'
                bombs_planted += 1

        for i in board:
            print(i)





#play the game
def play(dim_size = 10, num_bombs = 10):
    #Step 1: create the board and plant the bombs
    #Step 2: show the user the board and ask for where to dig
    #Step 3a: if the location is a bomb, show game over message
    #Step 3b: if location is not a bomb, dig recursiveley until each square is at least next to a bomb
    #Step 4: repeat steps 2 and 3 until there are no more places to dig -> Victory
    pass

new_board = Board(10, 10)
new_board.make_new_board()
