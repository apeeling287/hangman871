
from milestone_2 import random_word_generator

# def ask_for_input():  ##takes input from user and validates it 
#     while True:
#         user_guess = input("hPlease enter a letter: ")
#         if len(user_guess) == 1 and user_guess.isalpha():
#             break
#         else: 
#             print("Invalid letter. Please, enter a single alphabetical character") 
#     check_guess(user_guess)


def check_guess(guess):  #if statement that checks if the guessed letter is in the word.
    guess = guess.lower()
    random_word = random_word_generator(word_list)
    word_guessed = [x.replace(x, "_") for x in random_word]
    print(word_guessed)
    if guess in random_word:
        print(f"Good guess! {guess} is in the word")
        for index, letter in enumerate(random_word):
            if letter == guess:
                print(letter)
                word_guessed[index] = guess
            

                #word_guessed = word_guessed.replace(, guess)  
    else: 
        print(f"Sorry {guess} is not in the word. Try again")

word_list = ["mango", "passionfruit", "papaya", "blueberries", "oranges"] 

def ask_for_input_vtwo():  ##takes input from user and validates it 
    while True:
        user_guess = input("Please enter a letter: ")
        if not len(user_guess) == 1 and user_guess.isalpha():
            print("invalid letter. please enter a single alphabetical letter")
        elif user_guess in list_of_guesses:
            print("You already tried that letter!")
        else:    
            check_guess(user_guess)
            list_of_guesses.append(user_guess)

list_of_guesses = []
ask_for_input_vtwo()
#check_guess(guess)