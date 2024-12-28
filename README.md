## Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

step 1: The code takes in a list of words and randomly selects one word from this list 

step 2: The code then asks the user to input a letter and it then checks whether this letter is within the word which was randomly selected from the list 

step 3: If the letter which was guessed is in the random word, the _ in the word guessed list is replaced with the guess. E.g. ["_","_"."_","_"] is changed to ["_", "_", "a", "_"] with the guess at the corresponding index

step 4: The num_letters is equal to the number of unique letters in the random word and this will reduce every time a letter is correctly guessed

step 5: if a letter is incorrectly guessed, the number of lives will reduce by 1 and the game will end of the number of lives is equal to 0

step 6: inside the play_game function an instance of the Hangman class is created, inside the while loop it is checked whether the player has 0 lives left which will break out of the loop if true, it then checks if there are still letters remaining to guess, which if true will ask for another guess, and if the number of lives is not 0 and all letters have been guessed, the player wins the game!
It also prints the full word which has been guessed