
from random_word import RandomWords

class Hangman:
    pics =[
        '''
        + ---
        |   
        |
        |
        |
       ===
        ''',
        '''
        + --
        |   O
        |
        |
        |
       ===
        ''',
        '''
         + --
        |   O
        |   |
        |
        |
       ===
        ''',

        '''
         + --
        |   O
        |  /|
        |
        |
       ===
        ''',
        '''
         + --
        |   O
        |  /|\\
        |
        |
       ===
        ''',
        '''
         + --
        |   O
        |  /|\\
        |  /
        |
       ===
        ''',
        '''
         + --
        |   O
        |  /|\\
        |  / \\
        |
       ===
        ''',
    ]

    def __init__(self):
        self.secretWord = RandomWords().get_random_word()
        self.life = 6
        self.correctLetters=set()
        self.mistakeLetters=set()
        self.gameFinish=False


    def lifes(self,life):
        return Hangman.pics[life]

    def displayletter(self):
        print("Guessing :",end=' ')
        display =''
        # display = ''.join(letter if letter in self.correctLetters else '_' for letter in self.secretWord )

        for letter in self.secretWord:
            if letter in self.correctLetters:
                display+=letter
            else:
                display+='_'
        print(display)


    def check_game_status(self):
        if self.correctLetters == set(self.secretWord):
            print()
            print("You Won !!")
            self.gameFinish =True
        elif self.life==0:
            print()
            print("You Lose !!")
            self.gameFinish =True
            print(f"Word :{self.secretWord}")



    def guessletter(self,letter):
        letter = letter.lower()
        # blanks = len(self.secretWord) * '_'
        # print(blanks)
        if letter in self.correctLetters:
            print("Correct letter already entered")
            return

        if letter in self.secretWord:
            self.correctLetters.add(letter)
            print("Good Guess !")

        else:
            self.mistakeLetters.add(letter)
            print(Hangman.pics[6 - (self.life - 1)])
            self.life -= 1
            print(f"You lost a life! Remaining lives: {self.life * '❤'}")

        self.displayletter()
        self.check_game_status()
        print()

    def play(self):
        print('------------------------------------')
        print("Welcome to Hagman game (by Cva): ")
        print('------------------------------------')
        print()

        while not self.gameFinish:
            letter = input("Guess a letter: ").strip().lower()
            if len(letter) != 1 or not letter.isalpha():
                print("Please enter a single valid letter.")
                continue
            self.guessletter(letter)














































