import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.random_word = random.choice(word_list)     # word to be guessed - picked from word list
        self.word_guessed = [x.replace(x, "_") for x in self.random_word]   #list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed
        self.num_letters = len(set(self.random_word))    #int - The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives    #int - The number of lives the player has at the start of the game.
        self.word_list = word_list   # list - A list of words
        self.list_of_guesses = []   #list - A list of the guesses that have already been tried. Set this to an empty list initially
        print(f"The mystery word has {len(self.random_word)} characters")
        
    def check_guess(self, guess):  
        '''
        if statement that checks if the guessed letter is in the word.
        '''
        guess = guess.lower() 
        if guess in self.random_word:
            print(f"Good guess! {guess} is in the word")
            for index, letter in enumerate(self.random_word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1     
            print(self.word_guessed)     
            print(f"you have {self.num_letters} remaining to guess")
        else: 
            print(self.word_guessed)
            print(f"Sorry {guess} is not in the word. Try again") 
            self.num_lives -= 1
            print(f"you have {self.num_lives} lives left")    
                     
    

    def ask_for_input(self): 
        '''
        takes input from user and validates it 
        '''
        while True:
            user_guess = input("Please enter a letter: ")
            if len(user_guess) != 1 or not user_guess.isalpha():
                print("invalid letter. please enter a single alphabetical letter")
            elif user_guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:    
                self.list_of_guesses.append(user_guess)
                self.check_guess(user_guess)
                print(f"List of letters used:  {self.list_of_guesses}")
                break



def play_game(word_list):
    '''
    first if statement checks if the player has no lives left
    elif statement checks if there are still letters to guess
    If no lives are lost and all letters are guessed, the player wins
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:   
            print("you lost!")
            print(f"The word was {game.random_word}")
            break
        elif game.num_letters > 0:    
            game.ask_for_input()
        else:       
            print("Congratulations you won the game!")             
            print(f"The word was {game.random_word}")
            break


if __name__ == "__main__":
    word_list = ["mango", "passionfruit", "papaya", "blueberries", "oranges"]
    play_game(word_list)

        
