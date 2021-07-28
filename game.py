import random   # library to randomly choose words from the list of words

import sys  # sys module provides access to the variables and functions that interact strongly with the interpreter

# Define a function to list the rules of the game
# def game_rules():
#     import 

# Define a function to run the game
def play_game():
    words = ['earth', 'uranus', 'saturn', 'jupiter', 'mars', 'pluto', 
            'neptune', 'venus', 'planets', 'moon', 'sun', 'stars',
            'orbit', 'space', 'astronaut', 'shuttle', 'rocket', 'universe']
    
    # Choose a random word from word list
    word = random.choice(words)
    
    print("\nYour word has {} letters. Try to guess them!".format(len(word)))
    
    guesses = "" 
    
    # indicate the number of chances allowed
    chances = len(word) + 2

    # Tell the user how many chances they have
    print("You have {} guesses.".format(chances))
     
    while chances > 0:
        
        # counts the number of times a user fails
        failed = 0
        
        # all characters from the word taking one at a time.
        for char in word:
            
            # If the user inputs a correct guess, display the letter in the correct position
            if char in guesses:
                print(char, end="" )
                
            else:
                print("_ ", end="" )
                
                # for every failed attempt, failure will be incremented by 1
                failed += 1

        if failed == 0:
            # If all the letters are guessed correctly before the user runs out of chances, then congrats!
            print("\n\nCongratulations {}, you win!!!".format(name))
            
            # prints the correct word
            print("\n\nThe word is: {}.".format(word))
            # ask if they would like to play again.
            play_again() 
        
        # instruct the user to choose a letter
        guess = input("\n\nChoose a letter: ")

        guess = guess[0] # Ensures only 1st letter entered is used if multiple are attempted.
        
        # every letter input will be stored in guesses
        guesses += guess
        
        # check input with the letter in word
        if guess not in word:
            
            chances -= 1
            
            # If user inputs an incorrect letter, display “sorry, try again” and display the number of guesses remaining.
            print("\nNope, try again. You have", + chances, "more guesses.")
                                            
            if chances == 0:
                print("Better luck next time.\n")
                play_again()

# Define a function to play the game again
def play_again(): 
    play_again = input("\nWould you like to play again?  ").lower()
    
    if play_again in ("yes", "y"):
        print("\nAwesome {}! Let's play again!".format(name))
        play_game()

    elif play_again not in ("yes", "y", "no", "n"):
        print("Please answer yes or no.")

    else:
        quit_game()

# Define a function to quit the game
def quit_game():
    print("\nThat's okay {}, perhaps another time.\n".format(name))
    sys.exit()


# Ask user to input their name.
name = input("Hello, what is your name? ")

# If the user does not enter a name, instruct them to do so in order to proceed.
while name == '':
    name = input("Enter a name to proceed: ")
 
# Greet user by name 
print("\nNice to meet you {}!".format(name))

while True: 
    # Ask user if they want to play a word game
    want_to_play = input("\nWould you like to play a game? ").lower()

    # If yes, introduce game, list rules, and start the game.
    if want_to_play in ("yes",  "y"):
        print("\nGreat {}, let's play STAR WORDS!".format(name))
        # game_rules()
        play_game()

    # If the response is anything other than yes or no, ask the user to try again.
    elif want_to_play not in ("yes", "y", "no", "n"):
        print("Please answer yes or no.")
        continue

    # If no, respond with “That’s too bad. Nice meeting you {name}” and end program.
    else:
        quit_game()