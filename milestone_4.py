class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives


    def method_1(self):   ##self represents this instance of the class 
        pass
    

my_instance = Hangman(["oramge", "apply", "pear"], 5)
#myinstance.method_name()
print(my_instance.word_list)