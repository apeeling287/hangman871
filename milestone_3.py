
from milestone_2 import random_word_generator

def ask_for_input():  ##takes input from user and validates it 
    while True:
        user_guess = input("hPlease enter a letter: ")
        if len(user_guess) == 1 and user_guess.isalpha():
            break
        else: 
            print("Invalid letter. Please, enter a single alphabetical character") 
    check_guess(user_guess)


def check_guess(char):  #if statement that checks if the guessed letter is in the word.
    char = char.lower()
    random_word = random_word_generator(word_list)
    if char in random_word:
        print(f"Good guess! {char} is in the word")
    else: 
        print(f"Sorry {char} is not in the word. Try again")

word_list = ["mango", "passionfruit", "papaya", "blueberries", "oranges"] 


ask_for_input()
#check_guess(guess)