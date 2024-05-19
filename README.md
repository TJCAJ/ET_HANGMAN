

# E.T Hangman - Game

# Introduction
This my third milestone project for Code Institute Full-stack development program: Python Terminal.<br><brZ>
ET Hangman is a Python terminal game, which runs in the Code Institute mock terminal on Heroku. The main goal of the game is to guess a word in order to find the word that the computer randomly selects. The main theme is inspired by the original film for both ANSI figures and choice of words for the random word list, that consists of 49 different names and things that are directly related to Steven Spielbergs original.

[Live Project Here](https://portfolio-project-3.herokuapp.com/)



## User Experience - UX

### User Stories

* As a website creator, I want to:
  
1. Build an easy app for the users to play the game.
2. Build a game that is both enjoyable and challenging for the players.
   
* As a new visitor, I want to:

1. Be able to understand the purpose of the App and start a new game.
2. Be able to follow the score, see the wrong and right letters appear once I take a turn, and see how many tries remain before the game is over.
3. Be able to watch my results and other players' results on the Leaderboard.
   
* As a returning visitor, I want to:

1. Be able to play the game again with a different word as chosen by the computer.
2. Be challenged and try to improve on my previous scores. 
3. Compare my scores with other users on the Leaderboard.
   
## Design

#### Colours
* The colours in the game are supplied by the Python Colorama Model

### Flowcharts 
![Flowcharts](./assets/images/readme/hangman-flowcharts.jpg)<br>
The logic and flow behind the game was not to hard, but at first I was thinking about making a game where you should guess numbers isnetad of words, that's why I updated my flowchart where the player should guess a number, to a more common solution where the player should guess a word. I created my flowcharts in [draw.io](https://www.drawio.com/) to help me with the logical flow throughout the application. Shown below.<br>

## Game Features

### ET Hangman Stage 1
![Game Feature](./assets/images/readme/hangman-feature-5.jpg)<br><br>

This feature displays where the main scene happens. Here the user can play and see the following information about the game:
* Numbers of letters chosen by the computer 
* Hangman stages
* Letters guessed right
* Letters guessed wrong
* Current score
* Current number of attempts
* Input to guess a letter or a full word
* Input letters to either guess a letter only or the full word

### ET Hangman Stage 2 

![Hangman Stage 2 ]()<br><br>
Any time the player guesses a wrong letter, a part of the hangman appears
* 1 letter guessed wrong, the player will see the E.T. hangman figure and the first part of the hangman:  a rope, in green.

### ET Hangman Stage 3

![Hangman Stage 3]()
* 2 letters guessed wrong the player will see the E.T. hangman figure and 2 parts of the hangman a rope and head in green.

### ET Hangman Stage 4

![Hangman Stage 4]()
* 3 letters guessed wrong the player will see the E.T. hangman figure and 3 parts of the hangman rope, head and torso in yellow.

### ET Hangman Stage 5

![Hangman Stage 5]()
* 4 letters guessed wrong the player will see the E.T. hangman figure and 4 parts of the hangman rope, head, torso and the right arm in yellow.

### ET Hangman Stage 6

![Hangman Stage 6]()
* 5 letters guessed wrong the player will see the E.T. hangman figure and 5 parts of the hangman, rope, head, torso and both arms in red. Also the alert message "Danger Zone" will be displayed.

### ET Hangman Stage 7

![Hangman Stage 7]()
* 6 letters guessed wrong and the player will see the E.T. hangman figure and 6 parts of the hangman rope, head, torso, both arms and left leg in red. Also the alert message "Danger Zone" will be displayed.

### ET Hangman Stage 8 - Lose
![Hangman Stage 8 - Lose]()
* 7 letters guessed wrong the player will see the full hangman and the game is over.

### ET Hangman Stage 9 - Win

![Hangman Stage 9 - Win]()
* If the player guessed the full word letter by letter, they will see this feature and will win the game and get 200 points.

### ET Hangman Stage 10 - Win Extra

![Hangman Stage 10 - Win Extra]()
* If the player guessed all the letters that appear in the word thereby completing the word or at least guessing no more than 3 correct letters before completing the full word, this feature will appear.

### Menu Options

![Menu Options]()
* In the end of the game users will have access to the menu where they can choose from these options: <br>
[A] - Play Again <br>
[B] - Leaderboard <br>
[C] - Exit Game

### Leaderboard
![Leaderboard]()
* The Leaderboard shows the 15 players with the best scores.

### Exit Game
![Exit Game]()
* The players will see this message if they will chose to exit the game by typing [C].

### How to Play
![How to Play]()<br>
![How to Play]()<br>
The player has 7 attempts to try to guess the right word by inputting letters or can try to input all the letters to correctly complete the full . The word is randomly chosen by the computer from a list of words that are directly related to the original E.T. film by Steven Spielberg.
* When the game starts the player can see how many letters are in the word [1] and the computer will ask the player to input a letter or a word [7].
* If the player guesses the right letter, they will see a message from the computer [8] the letter guessed displayed in the word length [3], the hangman stage will remain the same [2] and the score will increase by 25 points [5]
* If the player guesses a wrong letter, they will see a message from the computer [9] the letter guessed displayed in the wrong letters guesses [4], the hangman stage will turn to the next stage [2] and the number of attempts will decrease by 1 [6]
* When the player types an invalid input, they will see a message from the computer [10].
* If the user guesses the right word they will see the [Winner Feature](#Hangman-Stage-9---Win)
* If the player guessed the full word at once or at least no more than 3 letters guessed right before trying to guess the full word, they will win the game-winning 500 extra points and see this feature [Winner Feature / Extra Points](#Hangman-Stage-10---Win)
* 7 letters guessed wrong and the player will see the [Loser Feature](#Hangman-Stage-8---lose)





































![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
