import random
from tkinter import E

class Board():
    def __init__(self, dim_size, num_bombs):
        
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_board()

        self.dug = set() #if location dug has already been dug it will be in this set

    def make_board(self):
        board = [[None for _ in range(self.dim_size)]for _ in range(self.dim_size)]

        #plant bombs
            ##if bomb already planted skip and don't add to iteration

        bombs_planted = 0

        while bombs_planted < self.num_bombs:
            col = random.randint(0, self.dim_size - 1) # 0 - 9 in this example
            row = random.randint(0, self.dim_size - 1)

            if board[col][row] == '*':
                pass
            else:
                bombs_planted += 1
                board[col][row] = '*'


        return board

    def dig(self, loc):
        loc = '5, 3'
        loc = loc.split(',')
        col, row = int(loc[0]), int(loc[1])

        if (col, row) in self.dug:
            pass
        else:
            self.dug.add((col, row))

    def find_bombs(self, col, row):
        if self.board[col][row] == '*':
            print('\n\nGame Lost.')
        else:
            

    

    
        
new_board = Board(10, 10)

for i in new_board.board:
    print(i)