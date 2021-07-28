game_play = """ 
How to Play:
The computer randomly chooses a word from a pre-determined list of words. All of the 
words are related to space exploration, hence the name of the game. The word is
displayed as dashes equivalent to the number of letters it contains. The player will 
try to guess the word, one letter at a time. The player has a set number of 
attempts to guess letters. If the player guesses a letter that is in the word, the 
computer fills in the appropriate blank. If the letter is not in the word, the computer
instructs the player to try again and one attempt is exhausted. The player wins by
guessing all the letters correctly before all the attempts are exhausted.
"""

game_objective = """
Object of the Game:
Guess the word before you run out of attempts.
"""

print(game_play + game_objective)