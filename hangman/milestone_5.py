import random

word_list = ['pineapple', 'lime', 'grape', 'mango', 'strawberry']
print(word_list)
word = random.choice(word_list)

class Hangman:
    '''
    This class is used to play a game of hangman.

    Parameters
    word - A word selected a random to be the target word for the game.
    word_guessed - The target word with each letter replaced by "_". The letter is revealed when guessed correctly.
    num_letters - The number of unique letters in the word.
    num_lives - The number of guesses the player is allowed to have before they lose. Set to five before the game.
    word_list - A list of fruits.
    list_of_guesses - The letters guessed by the player, stored in a list.
    
    '''
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = 5
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        '''

        This function checks the letter guessed against the letters in the target word.

        If correct input, the function prints that the player is correct.
        The function also displays the position of the letter in the target word.

        If the user is incorrect, one life is deducted and the user is notified that their answer is wrong.
        '''
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            self.num_letters = self.num_letters - 1
            for letter in range (len(self.word)):
                if guess == self.word[letter]:
                    self.word_guessed[letter] = guess
                    print(self.word_guessed)
                else:
                    pass
        else:
            self.num_lives = self.num_lives - 1
            print(f'Sorry, {guess} is not in the word. Try again.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        '''

        This function checks that the input is in the correct format.

        The program only accepts one lower case letter at a time.
        Anything else inputted result in an output telling the user the format is incorrect.

        If a letter has already been tried, a message is printed saying that they have already tried this letter.

        A valid guess is added to the guess list.
        '''
        while True:
            guess = input('Input a letter: ' )
            if guess.isalpha() == False or len(guess) > 1 or guess.isupper() == True:
                print('Invalid letter. Please, enter a single, lower case alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    '''
    
    This function asks for inputs, until they have won or lost.

    If the player runs out of lives, a message is printed, saying 'You lost!' and exits the program.

    If the player has guessed all of the letters in the word without losing all of their lives, they win.
    A congratulations message is displayed.
    '''
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break     
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break
        
play_game(word_list)