from collections import Counter

import random
from string import ascii_uppercase
import pyinputplus as pyip


user_id = 'X'
bot_id = 'O'







class Game():
    def __init__(self):
        self.user_id = 'X'
        self.bot_id = 'O'
        self.score = {'Win': 0, 'Loss': 0, 'Tie': 0}
        self.gameStart = True
        self.gameRun = True
        self.globalDict = {'O': {'A' : [], 'B': [], 'C': []}, 'X': {'A' : [], 'B': [], 'C': []}}
        self.values_available = [f'{alpha}{num}' for num in range(1, 4) for alpha in ascii_uppercase[:3]]
        self.letters_num = ascii_uppercase[0:3]
        
        
    def return_value(self, index):
        for i, v in self.globalDict.items():
            if index[1] in v[index[0]]:
                return i
        return ''



    #makes the grid for tic-tac-toe
    def grid(self):
        print('Board:\n\n')
        for letter in range(0, 3):
            for number in range (1 , 3):
                index = [self.letters_num[letter], number]
                print(self.return_value(index).center(5), end = '')
                print('|'.center(5), end = '')
            index = [self.letters_num[letter], 3]
            print(self.return_value(index).center(5), end = '')
            print('\n')

    #logic
    def add_grid(self, id: str, input):
        try:
            letter, number = str(input[0]).upper(), int(input[1])
            self.values_available.remove(letter + str(number))
            self.globalDict[id][letter].append(number)
            return True
        except Exception:
            return False 

    def game_win(self, id):
        self.gameRun = False

        if id == user_id:
            print('You win!!!')
            self.score['Win'] += 1
            
        else:
            print('Bot wins.')
            self.score['Loss'] += 1

    def span_board(self, dict):
        all_values = [i for x in dict.values() for i in x]
        count_num = Counter(all_values)
        try:
            most_common = count_num.most_common()[0][1]
            if most_common == 3:
                return True
        except:
            pass

        if (1 in dict['A'] and 2 in dict['B'] and 3 in dict['C']) or (1 in dict['C'] and 2 in dict['B'] and 3 in dict['A']):
            return True
        return False

    def bot(self):
        random_move = random.choice(self.values_available)
        self.add_grid(bot_id, random_move)

    def game_logic(self):
        win_dict = {'O': [], 'X': []}
        try:
            for id, v in self.globalDict.items():
                spanning_true = self.span_board(v) #will return true of cross row or vertical row condiiton is met
                for item, value in v.items():
                    straight_row = all(x in value for x in [1, 2, 3])
                    if straight_row:
                        break
                    
                if spanning_true or straight_row:
                    self.game_win(id)
        except:
            print('You tied.')
            self.score['Tie'] +=1
            self.gameRun = False


    def moves(self):
        while True:
            move = pyip.inputStr('Enter move: ')
            valid_move = self.add_grid(self.user_id, move)
            if valid_move == True:
                break
        self.bot()
        
    def clear_board(self):
        self.gameStart = True
        self.gameRun = True
        self.globalDict = {'O': {'A' : [], 'B': [], 'C': []}, 'X': {'A' : [], 'B': [], 'C': []}}
        self.values_available = [f'{alpha}{num}' for num in range(1, 4) for alpha in ascii_uppercase[:3]]

    def run(self):
        print('\nTic-Tac-Toe Game: \n\n' + '-'*45 + '\n')
        while self.gameStart:
            start = pyip.inputYesNo('Start new game: ')
            if start == 'yes':
                print('\n' * 40)
                while self.gameRun: 
                    self.grid()
                    print('\n')
                    self.moves()
                    print('\n\n\n\n\n\n\n\n')
                    self.grid()
                    self.game_logic()
                    print('\n')
                self.clear_board()
            else:
                self.gameStart = False
        print('\n' * 40)
        print('Score Board:'.center(50))
        print('-' * 50)
        print('')
        for score_name, score in self.score.items():
            print(f'{score_name}: {score}')
        


