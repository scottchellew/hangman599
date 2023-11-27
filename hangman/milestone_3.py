def check_guess(guess):  
    while True:
        guess = input('Input a letter ' )
        if guess.isalpha() == True:
            guess.lower()
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')

def ask_for_input(guess):
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')
    check_guess()

ask_for_input()