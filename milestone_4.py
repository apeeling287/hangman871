from milestone_2 import random_word_generator

class Hangman:
    def __init__(self, word, word_guessed, num_letters, word_list, list_of_guesses, num_lives):
        self.word = word    #The word to be guessed, picked randomly from the word_list
        self.word_guessed = word_guessed   #list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed
        self.num_letters = num_letters    #int - The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives    #int - The number of lives the player has at the start of the game.
        self.word_list = word_list   # list - A list of words
        self.list_of_guesses = list_of_guesses   #list - A list of the guesses that have already been tried. Set this to an empty list initially
        
    def check_guess(self, char):  #if statement that checks if the guessed letter is in the word.
        char = char.lower()
        random_word = random_word_generator(word_list)
        if char in random_word:
            print(f"Good guess! {char} is in the word")
        else: 
            print(f"Sorry {char} is not in the word. Try again")

    def ask_for_input_vtwo(self, check_guess):  ##takes input from user and validates it 
        while True:
            user_guess = input("hPlease enter a letter: ")
            if not len(user_guess) == 1 and user_guess.isalpha():
                print("invalid letter. please enter a single alphabetical letter")
            elif user_guess in list_of_guesses:
                print("You already tried that letter!")
            else:    
                check_guess(user_guess)
                list_of_guesses.append(user_guess)

list_of_guesses = []
#ask_for_input_vtwo()
word_list = ["mango", "passionfruit", "papaya", "blueberries", "oranges"] 

    

my_instance = Hangman(["oramge", "apply", "pear"], 5)
#myinstance.method_name()
print(my_instance.word_list)