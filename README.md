# Hangman
This is an version of the classic Hangman game, where the computer selects a word from a list and the user tries to guess it.

## Description
milestone_2.py - The code randomly selects a word from a list and asks the user to guess a letter. Input in the wrong format displays an error message to the user.

milestone_3.py - The code checks if the input is a letter, then checks if it matches a letter in the hangman word.

milestone_4.py combines milestone_2 and milestone_3. 
Furthermore, users are told if their choice is correct, incorrect or if it has been used before. Users can see the position of their letter in the word and how many lives they have left if they make an incorrect choice.

The final edit to this game is milestone_5.py. 
This takes the code of milestone_4.py and adds a while loop to track the amount of lives the user has left and the amount of letters left to guess. 
It prints whether they have won or lost the game and exits the game. 
Docstrings are added to milestone_5.py.

## Play
To play, in the terminal, access the hangman folder then type python milestone_5.py. Enter a single, lower case letter as a guess when prompted.

## Files
- milestone_2.py
- milestone_3.py
- milestone_4.py
- milestone_5.py
