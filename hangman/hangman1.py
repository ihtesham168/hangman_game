import random





class Hangman:
    
    def __init__(self,  word_list, num_lives=6):
        self.word = random.choice(word_list)
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed = ['_'] * len( self.word )
        self.list_letters = []
        self.num_letters=len(set(self.word))
        tries=6
        
        print("    Lets Play Hangman")
        
        
        print(f'The mystery word has {len(self.word)} characters')
        

        print(self.word_guessed)
     
        pass

    def check_letter(self, user_input) -> None:
        
        
        for index, letter in enumerate (self.word):

            if user_input in self.word[index]:
                self.word_guessed[index]=user_input
                
                
                pass
        if user_input in self.word:
            print(self.word_guessed)
            
            print('The letter is in the word')
            
            self.num_letters -= 1 

        elif user_input not in self.word :
            self.num_lives -= 1
            print(self.word_guessed)
            print(f' Number of live left {self.num_lives}')
            
            print("The letter is  not in the word")
            
            pass


        pass

    def ask_letter(self, list_letter):

        
       
        while True:
            
               
            letter =input (" Enter a single character ").lower()
            
            if len(letter) > 1:
                print(' Please enter just one character ')
                
            
            elif letter in list_letter:

                print('Letter is already in the list')


            elif len(letter)==1:
                list_letter.append(letter)
                print(f"Your Letters Guessed : {list_letter}" )
                
                self.check_letter(letter)
                break






            else:
                print('Please enter a character')


                

        pass

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    tries=6
    

    while game.num_lives > 0:
        game.ask_letter(game.list_letters)

        if game.num_lives== 0:
            

            

            print(f"Sorry, you ran out of tries. The word was {game.word}. Maybe next time!")
            
            


            break

        elif game.num_letters ==0:
           


            print("Congratulations, you guessed the word! You won!")
            
            
            break





    

    


    pass



if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    
    play_game(word_list)
# %%
