import random
# library to randomly choose words from the list of words

import sys

# Define a function to run the game
def play_game():
    words = ['earth', 'uranus', 'saturn', 'jupiter',
            'mars', 'pluto', 'neptune', 'venus',
            'planet', 'moon', 'sun', 'space']
    
    # will choose one random word from the words list
    word = random.choice(words)
    
    
    print("Guess the letters.")
    
    guesses = ''
    
    # indicate the number of turns allowed
    turns = 7
    
    
    while turns > 0:
        
        # counts the number of times a user fails
        failed = 0
        
        # all characters from the input
        # word taking one at a time.
        for char in word:
            
            # comparing that character with the character in guesses
            if char in guesses:
                print(char)
                
            else:
                print("_")
                
                # for every failed attempt, failure will be incremented by 1
                failed += 1
                
    
        if failed == 0:
            # user will win the game if failure is 0 and congratulations msg will be output
            print("Congratulations, you win!!!")
            
            # this prints the correct word
            print("The word is: ", word)
            break
        
        # if user has input the wrong letter then ask user to try again
        guess = input("Choose a letter: ")
        
        # every letter input will be stored in guesses
        guesses += guess
        
        # check input with the letter in word
        if guess not in word:
            
            turns -= 1
            
            # if the letter doesn’t appear in the word then “try again” will be output
            print("Nope, try again.")
            
            # this will print the number of guesses remaining
            print("You have", + turns, 'more guesses')
            
            
            if turns == 0:
                print("Better luck next time.")
                sys.exit()

    while True:
        play_again = input("Would you like to play again?  ").lower()
        
        if play_again == 'exit':
            quit_game()

        elif play_again not in ("yes", "y", "no", "n"):
            print("Please answer yes or no.")
            continue

        if play_again in ("yes", "y"):
            print("Great {}, let's play WORD PSYCHIC!".format(name))
            play_game()

        else:
            quit_game()


def quit_game():
    print("Thanks anyway {}, perhaps another time.".format(name))
    sys.exit()


name = input("Hello, what is your name? ")
# User inputs their name
 
print("Nice to meet you {}.".format(name))

while True:
    want_to_play = input("Would you like to play a game? ").lower()

    if want_to_play == 'exit':
        quit_game()

    elif want_to_play not in ("yes", "y", "no", "n"):
        print("Please answer yes or no.")
        continue

    if want_to_play in ("yes", "y"):
        print("Great {}, let's play WORD PSYCHIC!".format(name))
        play_game()

    else:
        quit_game()