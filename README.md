## Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The code takes in a list of words and randomly selects one word from this list 

The code then asks the user to input a letter and it then checks whether this letter is within the word which was randomly selected 

If the letter guessed is in the random word, the _ in the word guessed list is replaced with the guess. E.g. ["_","_"."_","_"] is changed to ["_", "_", "a", "_"] with the guess at the corresponding index

the num_letters is equal to the number of letters in the random word and this will reduce every time a letter is correctly guessed

**currently num_letters variable is not accessible from the function - need to figure out how to make it accessible**

**need to also reduce number of lives by one if wrong letter is guessed**