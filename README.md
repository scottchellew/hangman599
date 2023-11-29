# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

This has been a challenge, but it has made me feel more comfortable in using python. 

Currently the code randomly selects a word from a list and asks the user to guess a letter. Input in the wrong format displays an error message to the user.

Secondly, the code checks if the input is a letter, then checks if it matches a letter in the hangman word.

The third edit to the Hangman game is milestone_4.py. This is a combination of milestone_2 and milestone_3. Furthermore, users are told if their choice is correct, incorrect or if it has been used before. Users can see the position of their letter in the word and how many lives they have left if they make an incorrect choice.

The final edit to this game is milestone_5.py. This takes the code of milestone_4.py and adds a while loop to track the amount of lives the user has left and the amount of letters left to guess. It prints whether they have won or lost the game and exits the game.

To play, in the terminal, access the hangman folder then type python milestone_5.py. Enter a single, lower case letter as a guess when prompted.

files:
milestone_2.py
milestone_3.py
milestone_4.py
milestone_5.py