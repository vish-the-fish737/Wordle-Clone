When the game starts the user is presented with a grid of six rows with 5 boxes in each row. The objective of the game is for the user to guess the word the application has chosen. Words can only be 5 letters long.

Initially a "Guess" button is disabled. Once a player enters 5 letters, the button is enabled. If the user removes a character, which they can to change, then the Guess button is disabled again. 

When a player types a letter, it appears in upper case within a box in the currently active row. At the start, the first row is active. If a user presses any key other than a letter, the keystrokes are ignored.

When a user clicks on the "Guess" button the currently active row becomes inactive and any further input by the user will not affect the details on that row. The next row becomes active unless the user has completed all six rows or has won the game.

Once the "Guess" button is clicked, each box in the currently active row changes to a green, yellow, or gray color. It is green if the entered letter is in the exact location as it appears in the word to be guessed. It will be yellow if the letter appears in a different position. It will be gray if the letter is not present in the word to be guessed.

For example, given the word FAVOR, if the user enters RAPID, then the five boxes will have the colors Yellow, Green, GRAY, GRAY, GRAY, respectively.

If the user enters the next guess as MAYOR, the colors will be Gray, Green, Gray, Green, Green, respectively, in the second row.

Once the player wins they cant enter any more guess and will have to quit the game.

If the player guesses on the first try, display "Amazing". If the player guesses on the second try, display "Splendid". If they guess on a third try, display "Awesome". Win on any other tries, display "Yay". If the user fails to guess after six tries, display "It was FAVOR, better luck next time". Of course, if the word being guessed is something other than FAVOR, it will appears instead on that display line.

Please bring forward the practices, techniques, and tools you have learned so far. This includes: 
Good code quality
Lightweight design
Minimum code
Automated testing                                                         
Code coverage
Build files

A. When the game starts the word to guess will be picked in random from <https://agilec.cs.uh.edu/words>. Design in a way that if we decide to get the words from a different location in the future, then most of the code will not have to change, but new code may have to be written minimally to accommodate.

B. When a user presses the "Guess" button, check if the users input is a word with correct spelling by making a query to <http://agilec.cs.uh.edu/spellcheck?check=WORD> where WORD is replaced by the actual word the user enters. The site will return a true for correct spelling and false for an incorrect spelling. If the spelling is correct, continue to provide the feedback to the user for the word entered. If the guess is incorrect, display "Not a word." Design in a way that if we decide to check the spelling using a different service in the future, then most of the code will not have to change, but new code may have to be written minimally to accommodate.

The user can continue to edit the current guess if the word they entered is not a correct spelling. They do not lose a turn if they entered an incorrect spelling. Disable the "Guess" button until the user changes the word after entering a wrong spelling.
