import pyinputplus as pyip, string
from importingJSON import dictionary
from PyDictionary import PyDictionary
import time

class Hangman():
    def __init__(self, tries = 5, word = dictionary.pop(), definition = None):
        
        if type(word) == tuple:
            self.word = word[0].upper()
            self.definition = word[1]
        else:
            self.word = word.upper()
            self.definition = definition
        self.word_letters = set(self.word)
        self.game_run = True
        self.tries = tries
        

        self.counter = 0
        self.wins = 0
        self.losses = 0

        self.used_letters = set()

    def get_definition(self):
        if self.definition == None:
            pass
        else:
            print('HINT | DEFINITION: ')
            print(f'{self.definition}\n\n')

    def make_hangman(self):
        print(f'Tries left: {(self.tries - self.counter)}')
        print('Word Bank: ',end = '')
        for i in self.used_letters: print(f' {i} ', end = '')
        print('\n\n')
        words_correct = [f' {letter} ' if letter in self.used_letters else ' _ ' for letter in self.word]
        for i in words_correct: print(i, end = '')
        if (' _ ' in words_correct) == False:
            print('\n\n\nYou Won!!!!\n\n')
            self.game_run = False
            self.wins += 1
            
    
    def prompt(self):
        user_input = pyip.inputStr('\n\nInput a letter: ').upper()

        if len(user_input) > 1 and user_input == self.word:
            print('\n\n\n\n\n\n\n\n\n\n\n')
            print('Word: ', end = '')
            for i in self.word: print(i, end = ' ')
            print('\n\nYOU GUESSED THE WORD!!!')
            self.game_run = False
            self.wins +=1 
            print(f'Wins: {self.wins}')
        elif len(user_input) > 1 and user_input != self.word:
            self.counter += 1
        else:
            while len(user_input) > 1 or user_input in self.used_letters or user_input not in string.ascii_uppercase:
                if user_input in self.used_letters:
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou have already used this letter.\n\n')
                    self.make_hangman()
                else:
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNot a valid character.\n\n')
                    self.make_hangman()
                
                user_input = pyip.inputStr('\n\n\nInput a letter: ').upper()
        
            self.used_letters.add(user_input)
            
            if user_input not in self.word_letters:
                self.counter += 1

        
        

    def game(self):
        while self.game_run and self.counter < self.tries:
            print('\n\n\n\n\n\n\n\n\n\n\n')
                
            if (self.counter - 5) >= 0:
                self.get_definition()
            self.make_hangman()
            if self.game_run:
                print('\n')
                self.prompt()
                print('\n')
        if self.game_run == True:
            self.losses += 1
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou lost.')
            print(f'The word was {self.word}')

        
    def run(self):
        self.game()
        while True:
            user_input = pyip.inputYesNo('\n\nWant to play again? ')
            if user_input == 'yes':
                self.word, self.definition = dictionary.pop()
                self.word = self.word.upper()
                self.word_letters = set(self.word)
                self.counter = 0
                self.used_letters.clear()
                self.game_run = True
                self.game()
            else:
                break
        print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGames won: {self.wins}')

new_hangman = Hangman(10, 'test')

new_hangman.run()