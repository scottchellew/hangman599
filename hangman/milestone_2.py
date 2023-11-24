import random
word_list = ['Pineapple', 'Lime', 'Grape', 'Mango', 'Strawberry']
print(word_list)
word = random.choice(word_list)
print(word)
guess = input('Enter a single character: ')

if len(guess) == 1 and guess.isdigit() == False:
    print('Good guess!')
else:
    print('That is not a valid input.')

