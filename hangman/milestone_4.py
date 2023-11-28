import random

word_list = ['pineapple', 'lime', 'grape', 'mango', 'strawberry']
print(word_list)
word = random.choice(word_list)

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for i in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = 5
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            self.num_letters = self.num_letters - 1
            for i in range (len(self.word)):
                if guess == self.word[i]:
                    self.word_guessed[i] = guess
                    print(self.word_guessed)
                else:
                    pass
        else:
            self.num_lives = self.num_lives - 1
            print(f'Sorry, {guess} is not in the word. Try again.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        while True:
            guess = input('Input a letter ' )
            if guess.isalpha() == False or len(guess) > 1 or guess.isupper() == True:
                print('Invalid letter. Please, enter a single, lower case alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

hangman = Hangman(word_list, num_lives=5)
hangman.ask_for_input()