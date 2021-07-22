Game Process:

· Ask user to input their name.
· Greet user by name
· Ask user if they want to play a word game
	o If no, respond with “That’s too bad. Nice meeting you {name}” and end program
	o If yes, introduce game and list rules
· Ask the user if they want to proceed
	o If no, then respond with “Okay, maybe another time {name}” and end program
	o If yes, print “Good luck, {name}”
· Choose a random word  from word list
· Tell the user how many chances they have and instruct the user to choose a letter
	o if user inputs an incorrect letter, display “sorry, try again” and display the number of guesses remaining (total guesses – number of failed guesses)
	o if the user inputs a correct guess, display the letter in the correct position and instruct the user to choose another letter.
· Repeat the previous process until either all the letters have been guessed correctly or the user runs out of chances
	o If all the letters are guessed correctly before the chances are = 0 then display “Congratulations {name}, you win!” and ask if they would like to play again.
	o If the user runs out of chances without guessing the word, display “Sorry {name}, you lose!” and ask if they would like to play again.    
· If user wants to play again then start with choosing another random word and proceed through the processes.
If user does not want to play again, display “thanks for playing!” and exit the game.

Features Included:

   1. Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program -->
   2. Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
   3. Create a class, then create at least one object of that class and populate it with data. The value of at least one object must be used somewhere in your code
   4. Read data from an external file, such as text, JSON, CSV, etc and use that data in your application
   5. Implement a log that records errors, invalid inputs, or other important events and writes them to a text file
