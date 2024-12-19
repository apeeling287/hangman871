
import random

word_list = ["mango", "passionfruit", "papaya", "blueberries", "oranges"]  ##list of fruits
print(word_list)

def random_word_generator(input_list):
    word = random.choice(input_list)  ## a word is randomly chosen from the list 
    return word


# def is_a_letter(user_letter):                           ## function checks if user input is a single alphabetical letter 
#     if len(user_letter) == 1 and user_letter.isalpha():
#         print("good guess!")
#     else: 
#         print("Oops! That is not a valid input")   

# is_a_letter(guess)

