# ** Welcome to "Word Psychic" - a word guessing game

## ** How it Works:

1. Ask user to input their name.
	- If the user does not enter a name, instruct them to do so in order to proceed.
2. Greet user by name
3. Ask user if they want to play a word game
	- If no, respond with “That’s too bad. Nice meeting you {name}” and end program
	- If yes, introduce game, list rules, and start the game
4.  Choose a random word from word list
	- Tell the user how many chances they have and instruct the user to choose a letter
	- If user inputs an incorrect letter, display “sorry, try again” and display the number of guesses remaining (= total guesses – number of failed guesses)
	- If the user inputs a correct guess, display the letter in the correct position and instruct the user to choose another letter.
5.  Repeat the previous process until either all the letters have been guessed correctly or the user runs out of chances
	- If all the letters are guessed correctly before the user runs out of chances, then display “Congratulations {name}, you win!” and ask if they would like to play again.
	- If the user runs out of chances without guessing the word, display “Sorry {name}, you lose!” and ask if they would like to play again.    
		- If user wants to play again then start with choosing another random word and proceed through the processes.
		- If user does not want to play again, display “thanks for playing!” and exit the game.

## ** Features Included:

 * Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program.
	** ** -- The game will repeat until the user answers "n" when asked "Would you like to play again?"

 * Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
	** ** -- The game is played using a list that is named "words" which appears in lines 8-10.

 * Read data from an external file, such as text, JSON, CSV, etc and use that data in your application

 * Implement a log that records errors, invalid inputs, or other important events and writes them to a text file

 * Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, return a value to where it was called, and use that value somewhere else in your code. For example, you could create a function that reads how many items there are in a text file, returns that value, and later uses that value to execute a loop a certain number of times.
	** ** -- The functions defined are "play_game" (lines 7-88), "quit_game" (lines 91-93), and 

