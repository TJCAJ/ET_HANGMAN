![Wireframe](./assets/images/wireframe_et_hangman.png)

# E.T. Hangman - Game

# Introduction
This my third milestone project for Code Institute Full-stack development program: Python Terminal.<br><brZ>
ET Hangman is a Python terminal game, which runs in the Code Institute mock terminal on Heroku. The main goal of the game is to guess a word in order to find the word that the computer randomly selects. The main theme is inspired by the original film for both ANSI figures and choice of words for the random word list, that consists of 49 different names and things that are directly related to Steven Spielbergs original.

[Live Project Here](https://et-hangman-fb170fd57eab.herokuapp.com/)


## User Experience - UX

### User Stories

* As a website creator, I want to:

1. Build an easy app for the users to play the game.
2. Build a game that is both fun and challenging for the players.

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
![Flowcharts](./assets/images/et_hangman_flowchart.png)<br>
The logic and flow behind the game was not to hard, but at first I was thinking about making a game where you should guess numbers isnetad of words, that's why I updated my flowchart where the player should guess a number, to a more common solution where the player should guess a word. I created my flowcharts in [draw.io](https://www.drawio.com/) to help me with the logical flow throughout the application. Shown below.<br>


## Game Features

### ET Hangman Welcome Message

![Game Feature](./assets/images/et_hangman_welcome_message.png)

This is how the player is invited to the game with a fun and warm welcome message that also includes a brief description of how the game works and that E.T. needs the player's help with the password to his phone.


### ET Hangman Stage 1

<details>
<summary>ET hangman stage 1</summary>

![Game Feature](./assets/images/et_hangman_stage_1.png)
</details>

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

<details>
<summary>ET hangman stage 2</summary>

![Hangman Stage 2 ](./assets/images/et_hangman_stage_2.png)
</details>

Any time the player guesses a wrong letter, a part of the hangman appears
* 1 letter guessed wrong, the player will see the E.T. hangman figure and the first part of the hangman:  a rope, in green.


### ET Hangman Stage 3

<details>
<summary>ET hangman stage 3</summary>

![Hangman Stage 3](./assets/images/et_hangman_stage_3.png)
</details>

* 2 letters guessed wrong the player will see the E.T. hangman figure and 2 parts of the hangman a rope and head in green.


### ET Hangman Stage 4

<details>
<summary>ET hangman stage 4</summary>

![Hangman Stage 4](./assets/images/et_hangman_stage_4.png)
</details>

* 3 letters guessed wrong the player will see the E.T. hangman figure and 3 parts of the hangman rope, head and torso in yellow.


### ET Hangman Stage 5

<details>
<summary>ET hangman stage 5</summary>

![Hangman Stage 5](./assets/images/et_hangman_stage_5.png)
</details>

* 4 letters guessed wrong the player will see the E.T. hangman figure and 4 parts of the hangman rope, head, torso and the right arm in yellow.


### ET Hangman Stage 6

<details>
<summary>ET hangman stage 6</summary>

![Hangman Stage 6](./assets/images/et_hangman_stage_6.png)
</details>

* 5 letters guessed wrong the player will see the E.T. hangman figure and 5 parts of the hangman, rope, head, torso and both arms in red.


### ET Hangman Stage 7

<details>
<summary>ET hangman stage 7</summary>

![Hangman Stage 7](./assets/images/et_hangman_stage_7.png)
</details>

* 6 letters guessed wrong and the player will see the E.T. hangman figure and 6 parts of the hangman rope, head, torso, both arms and left leg in blue.


### ET Hangman Stage 8 - Lose

<details>
<summary>ET hangman stage 8</summary>

![Hangman Stage 8 - Lose](./assets/images/et_hangman_stage_8.png)
</details>

* 7 letters guessed wrong the player will see the a new E.T. figure in red and a message that states: "Wrong guess E:T: stays! The game is over and the correct word is revealed for the player while the total score is displayed.


### ET Hangman Stage 9 - Win

<details>
<summary>ET hangman stage 9</summary>

![Hangman Stage 9 - Win](./assets/images/et_hangman_stage_9.png)
</details>

* If the player guessed the full word letter by letter, they will see this feature and will win the game and get 350 points.


### ET Hangman Stage 10 - Win extra points

<details>
<summary>ET hangman stage 10</summary>

![Hangman Stage 10 - Win Extra](./assets/images/et_hangman_stage_10.png)
</details>

* If the player guessed all the letters that appear in the word thereby completing the word or at least guessing no more than 3 correct letters before completing the full word, this feature will appear and the player get 700 extra points.


### Menu Options

<details>
<summary>Menu options</summary>

![Menu Options](./assets/images/et_hangman_stage_abc.png)
</details>

* In the end of the game users will have access to the menu where they can choose from these options: <br>
[A] - Play Again <br>
[B] - Leaderboard <br>
[C] - Exit Game


### Leaderboard

<details>
<summary>Leaderboard</summary>

![Leaderboard](./assets/images/et_hangman_leaderboard.png)
</details>

* The Leaderboard shows the 15 players with the best scores.


### Exit Game

<details>
<summary>Exit Game</summary>

![Exit Game](./assets/images/et_hangman_closing_the_game.png)
</details>

* The players will see this message if they will chose to exit the game by typing [C]. (In this cas "Otis" has played the game.)


### How to Play
![How to Play](./assets/images/et_hangman_game_rules.png)<br>
![How to Play](./assets/images/et_hangman_stage_1.png)<br>
The player has 7 attempts to try to guess the right word by inputting letters or can try to input all the letters to correctly complete the full . The word is randomly chosen by the computer from a list of words that are directly related to the original E.T. film by Steven Spielberg.
* When the game starts the player can see how many letters are in the word [1] and the computer will ask the player to input a letter or a word [7].
* If the player guesses the right letter, they will see a message from the computer [8] the letter guessed displayed in the word length [3], the hangman stage will remain the same [2] and the score will increase by 25 points [5]
* If the player guesses a wrong letter, they will see a message from the computer [9] the letter guessed displayed in the wrong letters guesses [4], the hangman stage will turn to the next stage [2] and the number of attempts will decrease by 1 [6]
* When the player types an invalid input, they will see a message from the computer [10].
* If the user guesses the right word they will see the [Winner Feature](./assets/images/et_hangman_stage_9.png)
* If the player guessed the full word at once or at least no more than 3 letters guessed right before trying to guess the full word, they will win the game-winning 500 extra points and see this feature [Winner Feature / Extra Points](./assets/images/et_hangman_stage_10.png)
* 7 letters guessed wrong and the player will see the [Loser Feature](./assets/images/et_hangman_stage_8.png)


## Storage Data

### Leaderboard
I have used a Google sheet to save the player name, country, score and date. This sheet is connected to the code via Google Drive and Google Sheet API by the Google Cloud Platform. This allows me to send and receive data as I had access to the Google Sheet API credentials. I havel also added these in the Config Vars to these credentials as I deployed the project in Heroku. Since this is sensitive data, I have added the creds.json in the Git ignore file. This ensure that these credentials are not pushed to the repository.


### World Countries
I have also used a second Google sheet in order to validate the players country of origin. This sheet is of course also connected to the code via Google Drive and Google Sheet API by the Google Cloud Platform.

I found the list of countries at [gigasheet.com](https://app.gigasheet.com/spreadsheet/list-of-all-countries-in-the-world---spreadsheet/19c9919d_dc1b_41e2_90ea_540d0e241df7?referrerId=https%3A%2F%2Fwww.gigasheet.com%2Fsample-data%2Flist-of-all-countries-in-the-world---spreadsheet)


### Code to Connect to Google Sheet

<details>
<summary>Connect Google Sheet</summary>

![Code to Connect to Google Sheet](./assets/images/et_hangman_google_sheets_connection.png)
</details>


### Google Sheet Hangman Leaderboard

<details>
<summary>Google Sheet Leaderboard</summary>

![Google Sheet Hangman Leaderboard](./assets/images/et_hangman_leaderboard_google_sheet.jpg)
</details>


### Google Sheet World Countries

<details>
<summary>Google Sheet Countries</summary>

![Google Sheet World Countries](./assets/images/et_hangman_world_countries_google_sheet.jpg)
</details>


## Technologies Used

### Languages Used

* [Python](https://www.python.org/)


#### Python Packages

* [Random](https://docs.python.org/3/library/random.html?highlight=random#module-random): returns a random integer to get a random word
* [Datetime](https://pypi.org/project/DateTime/): returns the full date
* [Gspread](https://pypi.org/project/gspread/): allows communication with Google Sheets
* [Colorama](https://pypi.org/project/colorama/): allows terminal text to be printed in different colours / styles
* [datetime](https://pypi.org/project/datetime2/): adding the capability of constructing and representing date and time in many formats
* [google.oauth2.service_accoun](https://google-auth.readthedocs.io/en/stable/index.html): credentials used to validate credentials and grant access to Google service accounts


### Frameworks - Libraries - Programs Used

* [GitHub](https://github.com/)
    * GitHub is used to store the project's code after being pushed from Git
* [Heroku](https://id.heroku.com)
    * Heroku was used to deploy the live project
* [VSCode](https://code.visualstudio.com/)
    * VSCode was used to create and edit the website and to commit to Git and push to GitHub
* [draw.io](https://www.drawio.com/)
    * draw.io was used to create the flowchart
* [Pythonchecker](https://www.pythonchecker.com/)
    * Pythonchecker was used to validate all the Python code
* [Patorjk](https://patorjk.com)
    * Patorjk (ASCII Art Generator) was used to draw the titles for the game logos
* [ASCII Art Archive](https://www.asciiart.eu/image-to-ascii)
    * ASCII Art Archive was used to convert images for the game logos
* [Lambdatest](https://www.lambdatest.com/free-online-tools/python-beautifier)
    * Lambdatest was used to format my python code to a final finish


## Testing

### **Initial tests**

The primary goal for this project was for me to learn the basis of Python and build a command-line application that allows your users to register and play my own E.T. version of a hangman game that delivers a positive experience for the user. I have used Visual Studio Code to build the game and deployed to Heroku. I choosed to develop the game functions localy and test the most basic ones in various stages before I deployed and started to build the app in Heroku and run it as a command-line application.

- Macbook Pro (5120 X 2880)
- LG HDR 4K" Monitor (3840x2160)

<details>
<summary>Test Sheet Page 1</summary>

![test sheet page 1](./assets/images/et_test_validation%20sheet_et_hangman.jpg)
</details>

<details>
<summary>Test Sheet Page 2</summary>

![test sheet page 2](./assets/images/et_test_validation%20sheet_et_hangman_page_2.jpg)
</details>


### **Validation**
### PEP 8

- This validator was installed in VS with pip install pep8 and used to validate every Python file in the project to check for  syntax errors in the project. This was done with the command flake8 in VS. Information about this was found here: [pep8](https://pypi.org/project/pep8/) and here: [flake](https://pypi.org/project/flake8/) [flake8](https://flake8.pycqa.org/en/latest/)

- [CI_Python_Linter](https://pep8ci.herokuapp.com/) was also used to check all python files for errors, with no errors found.

<details>
<summary>CI Python Linter Validation</summary>

![Python Linter test](./assets/images/ci_python_linther_validation.png)
</details>

### codeWOF

 [CodeWOF](https://www.codewof.co.nz/style/python3/) was used to test code against the main conventions recommended for Python in PEP 8.

 ### Lighthouse

 <details>
<summary>Lighthouse Scores for Desktop</summary>

![desktop lighthouse scores](./assets/images/lighthouse_test_et_hangman_game.png)
</details>


## Deploying this Project

* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
7. Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button
8. Click Reveal Config Vars again and enter CREDS into the Key box and the Google credentials into the Value box
9. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
10. Repeat step 8 to add node.js. o Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order
11. Scroll to the top of the page and choose the Deploy tab
12. Select Github as the deployment method
13. Confirm you want to connect to GitHub
14. Search for the repository name and click the connect button
15. Scroll to the bottom of the deploy page and select the preferred deployment type
16. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github


## Forking This Project

* Fork this project by following the steps:

1. Open [GitHub](https://github.com/)
2. Click on the project to be forked
3. Find the Fork button at the top right of the page
4. Once you click the button the fork will be in your repository


## Cloning This Project

* Clone this project by following the steps:

1. Open [GitHub](https://github.com/)
2. Click on the project to be cloned
3. You will be provided with three options to choose from, HTTPS, SSH, or GitHub CLI, click the clipboard icon in order to copy the URL
4. Once you click the button the fork will be in your repository
5. Open a new terminal
6. Change the current working directory to the location that you want the cloned directory
7. Type git clone and paste the URL copied in step 3
8. Press Enter and the project is cloned


## Credits

- Structure and basic logic for the game, [PedroCristo](https://github.com/PedroCristo/portfolio_project_3)

- Clear screen function - via [Stack overflow](https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console) and thanks to Peter Mortensen.

- Python Raw Strings - [Python tutorial](https://www.pythontutorial.net/python-basics/python-raw-strings/)

- Python Interpolation and Formatting - [Real_Python](https://realpython.com/python-f-strings/)

- Remove empty lines from a string - [Sling Academy](https://www.slingacademy.com/article/python-3-ways-to-remove-empty-lines-from-a-string/)

- Trim Trailing White Space - [Visual studio code user_guide](https://code.visualstudio.com/docs/editor/codebasics#_trim-trailing-whitespace)

- Center Welcome message in Terminal - [Stack Overflow](52138936/how-to-center-text-in-python-3-after-an-input) and thanks to Joe Iddon.


### Information Sources / Resources / References

  ### All the content in the game is original

- [Code Institute](https://codeinstitute.net/ie/) for their Love Sandwishes learning material.

- [W3Schools](https://www.w3schools.com/) for additional learning material overall.

- [Code Institute - Template](https://github.com/Code-Institute-Org/python-essentials-template) The terminal function and template for the deployable application

- [distansakademin - Youtube videos](https://www.youtube.com/watch?v=IWx4gnv0L0o&t=3s) Basics in Python

- [Stack Overflow](https://stackoverflow.com/) Various tips and references

- [pypi.org](https://pypi.org/) Python Packages

- [Canva](https://www.canva.com/) made it possible to make a nice wireframe



### **Acknowledgements**

I would like to thank my mentor Gareth Mc Girr for his continued guidance and expertise, my fellow classmates and Cohort Facilitator Kristyna Wach as well as the extended Code Institute Slack community where I found many answers to my questions just by searching previous threads.
