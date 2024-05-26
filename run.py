"""This file runs the ET Hangman game."""

# Modules and libraries
import datetime
import os
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, init
from et_hangman_words import get_word
from et_hangman_art import stages, hangman_logo, game_info

# Setup for Colorama
init(autoreset=True)


# Define clear screen function
def cls():
    os.system("cls" if os.name == "nt" else "clear")


# Function to clean the prompt from empty lines
def clean_prompt(prompt):
    lines = prompt.split("\n")
    cleaned_lines = []

    for line in lines:
        line = line.rstrip()
        if line:
            cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


# Getting today's date
DATE = datetime.datetime.today().strftime("%Y-%m-%d")

# Google Sheets API setup
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# Authorization for Google Sheets API
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("ET_Hangman_Leaderboard")
# Open world countries sheet
COUNTRIES_SHEET = GSPREAD_CLIENT.open("world_countries").sheet1

# Getting the leaderboard worksheet
leaderboard = SHEET.worksheet("leaderboard")

# Getting the world countries worksheet
countries = COUNTRIES_SHEET.col_values(1)

# Constants for scoring
CORRECT_GUESSED = 25
EXTRA_SCORE = 200
FULLY_WORD_SCORE = 500

# Message for playing again
PLAY_AGAIN_MSG = f"""{Fore.CYAN}
A - PLAY AGAIN
B - LEADERBOARD
C - EXIT THE GAME
"""


# Function to validate a country
def validate_country(country_name, country_list):
    """
    Validate the country names against the list of countries
    """
    return country_name.upper() in [country.upper()
                                    for country in country_list]


# Function to validate player's name
def validate_name(name):
    """
    Validate the player's name.
    Name must not be empty and can only contain letters, max 6 characters long
    """
    return name.isalpha() and 0 < len(name) <= 6


# Function to display hangman stages
def display_hangman(tries):
    """
    Display hangman stages from the start of the game
    and change anytime the player doesn't guess the right letter
    """
    cleaned_stages = clean_prompt(stages[tries])
    print(cleaned_stages)


# Function to add space between letters in the word
def word_space(full_word):
    """
    Add space in between letters in the random word
    """
    for i in full_word:
        print(i, end=" ")


# Function to display player score
def display_score(score):
    """
    Display player score during the game
    """
    print(f"\tSCORE: {score}")


# Function to update the leaderboard
def update_worksheet(name, score, country):
    """
    Update a new row in the Hangman worksheet.
    This updates a new row with the rank, name, date, score, and country.
            name (string): Player Name.
            score (int): Score.
            country (string); Player's Country.

            Returns;
                no return
    """

    print("\t{}Updating Leaderboard...\n".format(Fore.GREEN))

    # Get all values in the worksheet
    all_values = leaderboard.get_all_values()
    # Determine the next rank
    rank = len(all_values)

    # Append the new row with rank, name, date, score, and country
    leaderboard.append_row([rank, name, DATE, score, country])
    print(f"\t{Fore.GREEN}Leaderboard Update successful.\n")


def display_leaderboard():
    """
    Displays the players 15 best scores
    """
    score_sheet = leaderboard.get_all_values()[1:]

    update_data = sorted(score_sheet, key=lambda x: int(x[3]), reverse=True)

    # Column headers
    headers = ["POS", "NAME", "DATE", "SCORE", "COUNTRY"]

    separator_length = 50

    # Print the headers and table in better columns
    print("=" * separator_length)
    print(
        f"{Fore.YELLOW} {headers[0]:<5} {headers[1]:<10} {headers[2]:<15} "
        f"{headers[3]:<6} {headers[4]:<8}"
    )
    # Print each row of data for better display
    print("=" * separator_length)
    for i, row in enumerate(update_data[:15], start=1):
        print(
            f"{Fore.GREEN} {i:<5} {row[1]:<10} {row[2]:<15} "
            f"{row[3]:<6} {row[4]:<8}"
        )

    print("=" * separator_length)


# Function to display the welcome message
def welcome():
    print(Fore.LIGHTGREEN_EX + hangman_logo[0])
    print(Fore.YELLOW + "\nWelcome to the E.T. Hangman Game!")
    print(Fore.YELLOW + "Try to guess a name or a word, one letter at a time.")
    print(Fore.YELLOW + "You have a limited number of guesses, \
        so choose wisely!")


# Function to play the game
def game(random_word, player_name, player_country):
    """
    Game main function
    """
    full_word = "_" * len(random_word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    guessed_wrong = []
    guessed_right = 0
    attempts = 7
    score = 0
    print(f"{Fore.LIGHTYELLOW_EX}\n\tLET'S PLAY THE HANGMAN GAME!\n")
    print(
        f"""{Fore.LIGHTYELLOW_EX}\t
    YOU HAVE TO GUESS A WORD WITH {len(random_word)} LETTERS"""
    )
    print(display_hangman(attempts))
    word_space(f"\t{full_word}")
    print("\n")
    while not guessed and attempts > 0:
        print(f"{Fore.RED}\n\tWRONG LETTERS GUESSED:\n\t{guessed_wrong}\n")
        display_score(score)
        print(
            f"""\n{Fore.LIGHTBLUE_EX}
        ================================================="""
        )
        if attempts > 1:
            print(f"{Fore.LIGHTYELLOW_EX}\n\tYOU HAVE {attempts} ATTEMPTS")
        else:
            print(f"{Fore.RED}\n\tYOU HAVE {attempts} ATTEMPT LEFT\n")
        guess = input(
            f"""{Fore.LIGHTBLUE_EX}\t\t
        GUESS A LETTER OR A WORD PLEASE:\n\t>>> """
        ).upper()
        print(
            f"""\n{Fore.LIGHTMAGENTA_EX}
        ================================================="""
        )
        # Check if the player has already guessed the letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(
                    f"""{Fore.LIGHTYELLOW_EX}\n\t
                YOU HAVE ALREADY GUESSED THIS LETTER {guess}\n"""
                )
            elif guess not in random_word:
                print(
                    f"""{Fore.RED}\n\t
                {guess} IS NOT IN THE WORD. TRY ANOTHER ONE!\n"""
                )
                attempts -= 1
                guessed_letters.append(guess)
                guessed_wrong.append(guess)
            else:
                print(
                    f"""{Fore.GREEN}\n\t
                GREAT, {guess} IS IN THE WORD! KEEP GOING!\n"""
                )
                guessed_letters.append(guess)
                guessed_right += 1
                score += CORRECT_GUESSED
                word_as_list = list(full_word)
                indices = [i for i, letter in enumerate(
                    random_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                full_word = "".join(word_as_list)
                if "_" not in full_word:
                    guessed = True
        elif len(guess) == len(random_word) and guess.isalpha():
            if guess in guessed_words:
                print(
                    f"""{Fore.LIGHTRED_EX}\n\t
                YOU HAVE GUESSED THE WORD {guess} ALREADY."""
                )
            elif guess != random_word:
                print(f"{Fore.LIGHTRED_EX}\n\t{
                      guess}, IS NOT THE WORD. TRY AGAIN!")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                full_word = random_word
        else:
            cls()
            print(f"{Fore.LIGHTRED_EX}\n\tIS NOT VALID GUESS.\n")
        print(display_hangman(attempts))
        word_space(f"\t{full_word}")
        print("\n")
    final_result(
        guessed, random_word, guessed_right, score, player_name, player_country
    )


# Function to display the final result
def final_result(guessed, random_word, guessed_right, score, name, country):
    """
    Check if the player loses or won the game guessing the word letter
    by letter or the word at once
    """
    if guessed and len(random_word) >= 6 and guessed_right <= 3:
        result_message = f"""{Fore.GREEN}{hangman_logo[3]}
        YOU WIN {name}, YOU HAVE GUESSED THE WORD COMPLETELY AT ONCE!\n"""
        score = score + EXTRA_SCORE + FULLY_WORD_SCORE
    elif guessed:
        result_message = f"""{Fore.GREEN}{hangman_logo[2]}
        YOU WIN {name}, YOU HAVE GUESSED THE RIGHT WORD!\n"""
        score = score + EXTRA_SCORE
    else:
        result_message = f"""{Fore.RED}{hangman_logo[1]}
        YOU LOSE {name}, THE RIGHT WORD WAS {random_word}!"""

    # Clean the result message
    cleaned_result_message = clean_prompt(result_message)

    print(cleaned_result_message)
    update_worksheet(name, score, country)
    display_score(score)


# Main function to control the game flow
def main():
    """
    Starts the game with a random word.
    Once a game run is complete, give to the player 3 choices at the end:
        * Play again
        * Leaderboard
        * Exit the game
    """
    play_game = True
    while True:
        if play_game:
            random_word = get_word()
            game(random_word, player_name, player_country)

        user_input = input(PLAY_AGAIN_MSG + ">>> ").upper()
        if user_input == "A":
            print("\n\tYou have decided to continue playing the game.\n")
            play_game = True
        elif user_input == "B":
            display_leaderboard()
            play_game = False
        elif user_input == "C":
            print(f"{Fore.LIGHTRED_EX}\n\tNow closing the game...")
            print(
                f"""{Fore.LIGHTCYAN_EX}
            \n\tThanks for playing, {player_name.capitalize()}.
            \n\tHope to see you again soon!\n"""
            )
            break
        else:
            cls()
            print(
                f"""{Fore.YELLOW}\n\t
            That is not a valid option. Please try again.\n"""
            )
            play_game = False


if __name__ == "__main__":
    welcome()
    input(f"""\n{Fore.CYAN}PRESS ANY KEY TO START THE GAME.\n>>> """)
    # Allows the user to input their own name and country to play the game
    while True:
        player_name = input(
            f"\n{Fore.CYAN}NAME (max 6 letter):\n>>> ").strip().upper()
        if not validate_name(player_name):
            print(f"{Fore.RED}This is not a valid name! \
                Ensure it is max 6 letters")
            continue
        else:
            break
    while True:
        player_country = input(
            f"{Fore.CYAN}YOUR COUNTRY:\n>>> ").strip().upper()
        if len(player_country) == 0 or not validate_country(
            player_country, countries
        ):
            print(f"{Fore.RED}This is not a valid country!")
            continue
        else:
            break
    print(
        f"""{Fore.YELLOW}\n\t
    HELLO {player_name}, WELCOME TO THE HANGMAN GAME!\n"""
    )
    print(f"{Fore.LIGHTBLUE_EX}{game_info[0]}")
    input(
        f"""\n{Fore.CYAN}
    {player_name}, PRESS ANY KEY TO START THE GAME.\n    >>> """
    )

    main()
