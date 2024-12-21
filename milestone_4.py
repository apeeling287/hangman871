from milestone_2 import random_word_generator

class Hangman:
    def __init__(self, word_list, num_lives=5):
        #self.word = word   
        self.random_word = random_word_generator(word_list)     # word to be guessed - picked from word list
        self.word_guessed = [x.replace(x, "_") for x in self.random_word]   #list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed
        self.num_letters = len(set(self.random_word))    #int - The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives    #int - The number of lives the player has at the start of the game.
        self.word_list = word_list   # list - A list of words
        self.list_of_guesses = []   #list - A list of the guesses that have already been tried. Set this to an empty list initially
        self.random_word = random_word_generator(word_list)     # word to be guessed - picked from word list

        
    def check_guess(self, guess):  #if statement that checks if the guessed letter is in the word.
        guess = guess.lower() 
        if guess in self.random_word:
            print(f"Good guess! {guess} is in the word")
            for index, letter in enumerate(self.random_word):
                if letter == guess:
                    print(letter)
                    self.word_guessed[index] = guess
                    print(self.word_guessed)
            self.num_letters -= 1
            print(self.num_letters)
        else: 
            print(f"Sorry {guess} is not in the word. Try again") 
            self.num_lives -= 1
            print(f"you have {self.num_lives} lives left")                     
    

    def ask_for_input_vtwo(self):  ##takes input from user and validates it 
        while True:
            user_guess = input("Please enter a letter: ")
            if not len(user_guess) == 1 and user_guess.isalpha():
                print("invalid letter. please enter a single alphabetical letter")
            elif user_guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:    
                self.check_guess(user_guess)
                self.list_of_guesses.append(user_guess)

word_list = ["mango", "passionfruit", "papaya", "blueberries", "oranges"] 

my_instance = Hangman(["oramge", "apple", "pear"], 5)
my_instance.ask_for_input_vtwo()
#myinstance.method_name()
