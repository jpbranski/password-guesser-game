# WORD GUESS HACKING GAME
#### Video Demo: https://youtu.be/_yMxPPPwe1A
#### Description:

Inspired by the terminal minigame in Bethesda Game Studio's _Fallout_ series, take on the roll of guessing the password to access secrets within locked terminals.

At its core, this project is a word guessing game from a randomly selected list of words. Throw in user input for difficulty, as well as some other random functions, this simple game will be a different experience for players every time they run it.

## How to play
In order to play, you will first need to run `python project.py`. Following that you will have two prompts, one for your username, and one for the difficulty. The difficulty scales from 1-5, and changes the length of the words to be used for passwords. A scrambled block of symbols will have a random list of words scattered throughout, with one of them being the correct password. When you type in your guess, you will get notified if it is a correct guess, or a wrong guess. If the guess is wrong, it will tell you how similar you word is compared to that of the correct answer. When you win, it will tell you your total number of guesses, as well as your final score. Additionally, it will prompt you if you want to play again.

## Imports
- random
- string
- sys
- textwrap

## Logic
The logic of the game utilizes multiple different functions and methods, both ones talked about throughout CS50P and other new ones. It relies heavily on the `random` import for creating a unique experience, while `string` and `textwrap` help create the feel of "screen" itself.

Additionally, how the functions and files are written allow the game to be easily scaled. Highscores, larger variety of words, more difficulties, or even different styles of scrambled boards could all be implemented with only minimal changes. The choice to not include a highscores currently is due to the localization of the file, rather than it being properly hosted.

The board itself is a string. When it reprints (after a guess), the new lines are removed and readded after the characters are replaced. Unless you have a terminal window opened to be very tall, it can give the appearance that the board is just "replacing" the text in place!

### Other design choices
The score is an arbitrary value pieced together to give different weights to different difficulties. A difficulty 5 victory will almost always surpass a difficulty 1 or 2 due to the multiplier.


