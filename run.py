"""This file runs the ET Hangman game."""

# Modules and libraries
import datetime
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, init
from et_hangman_words import get_word
from et_hangman_art import stages, hangman_logo, game_info

# Setup for Colorama
init(autoreset=True)

# Getting today's date
date = str(datetime.date.today)

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

# Getting the leaderboard worksheet
leaderboard = SHEET.worksheet("leaderboard")

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


# Function to display hangman stages
def display_hangman(tries):
    """
    Display hangman stages from the start of the game
    and change anytime the player doesn't guess the right letter
    """
    return stages[tries]


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
    """
    print(f"\t{Fore.GREEN}Updating Leaderboard...\n")

    # Get all values in the worksheet
    all_values = leaderboard.get_all_values()
    # Determine the next rank
    rank = len(all_values)

    # Append the new row with rank, name, date, score, and country
    leaderboard.append_row([rank, name, date, score, country])
    print(f"\t{Fore.GREEN}Leaderboard Update successful.\n")


# Getting the leaderboard worksheet
leaderboard = SHEET.worksheet("leaderboard")


def display_leaderboard():
    """
    Displays the players 15 best scores
    """
    score_sheet = leaderboard.get_all_values()[1:]
    for data in score_sheet:
        data[3] = data[3]

    update_data = sorted(score_sheet, key=lambda x: int(x[3]), reverse=True)

    print(f"{Fore.YELLOW}============================================================")
    print(f"{Fore.YELLOW}\n\tPOS\tNAME\tDATE\t\tSCORE\tCOUNTRY")
    print(f"{Fore.YELLOW}============================================================")

    count = min(len(update_data), 15)
    for i in range(count):
        print(
            f"""
        {Fore.GREEN}{i+1}\t{update_data[i][1]}\t{update_data[i][2]}\t{
        update_data[i][3]}\t{update_data[i][4]}"""
        )
    print(f"{Fore.YELLOW}============================================================")


# Function to play the game
def game(random_word):
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
    print(f"{Fore.YELLOW}\n\tLET'S PLAY THE HANGMAN GAME!\n")
    print(
        f"""{Fore.YELLOW}\t
    YOU HAVE TO GUESS A WORD WITH {len(random_word)} LETTERS"""
    )
    print(display_hangman(attempts))
    word_space(f"\t{full_word}")
    print("\n")
    while not guessed and attempts > 0:
        print(f"{Fore.RED}\n\tWRONG LETTERS GUESSED:\n\t{guessed_wrong}\n")
        display_score(score)
        print(
            f"""\n{Fore.CYAN}
        ================================================="""
        )
        if attempts > 1:
            print(f"{Fore.YELLOW}\n\tYOU HAVE {attempts} ATTEMPTS")
        else:
            print(f"{Fore.RED}\n\tYOU HAVE {attempts} ATTEMPT LEFT\n")
        guess = input(
            f"""{Fore.CYAN}\t\t
        GUESS A LETTER OR A WORD PLEASE:\n\t>>> """
        ).upper()
        print(
            f"""\n{Fore.CYAN}
        ================================================="""
        )
        # Check if the player has already guessed the letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(
                    f"""{Fore.YELLOW}\n\t
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
                indices = [i for i, letter in enumerate(random_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                full_word = "".join(word_as_list)
                if "_" not in full_word:
                    guessed = True
        elif len(guess) == len(random_word) and guess.isalpha():
            if guess in guessed_words:
                print(
                    f"""{Fore.YELLOW}\n\t
                YOU HAVE GUESSED THE WORD {guess} ALREADY."""
                )
            elif guess != random_word:
                print(f"{Fore.RED}\n\t{guess}, IS NOT THE WORD. TRY AGAIN!")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                full_word = random_word
        else:
            print(f"{Fore.YELLOW}\n\tIS NOT VALID GUESS.\n")
        print(display_hangman(attempts))
        word_space(f"\t{full_word}")
        print("\n")
    final_result(guessed, random_word, guessed_right, score)


# Function to display the final result
def final_result(guessed, random_word, guessed_right, score):
    """
    Check if the player loses or won the game guessing the word letter
    by letter or the word at once
    """
    if guessed and len(random_word) >= 6 and guessed_right <= 3:
        print(f"{Fore.GREEN}{hangman_logo[3]}")
        print(
            f"""{Fore.GREEN}
        YOU WIN {player_name}, YOU HAVE GUESSED THE WORD COMPLETELY AT ONCE!\n
        """
        )
        score = score + EXTRA_SCORE + FULLY_WORD_SCORE
    elif guessed:
        print(f"{Fore.GREEN}{hangman_logo[2]}")
        print(
            f"""{Fore.GREEN}
        YOU WIN {player_name}, YOU HAVE GUESSED THE RIGHT WORD!\n
        """
        )
        score = score + EXTRA_SCORE
    else:
        print(f"{Fore.RED}{hangman_logo[1]}")
        print(
            f"""{Fore.RED}
        YOU LOSE {player_name}, THE RIGHT WORD WAS {random_word}!
        """
        )
    update_worksheet(data, score)
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
            game(random_word)

        user_input = input(f"{PLAY_AGAIN_MSG}>>> ").upper()
        if user_input == "A":
            print(f"\n\tYou have decided to continue playing the game.\n")
            play_game = True
        elif user_input == "B":
            display_leaderboard()
            play_game = False
        elif user_input == "C":
            print(f"{Fore.RED}\n\tNow closing the game...")
            print(
                f"""{Fore.CYAN}
            \n\tThanks for playing, {player_name.capitalize()}.
            \n\tHope to see you again soon!\n"""
            )
            break
        else:
            print(
                f"""{Fore.YELLOW}\n\t
            That is not a valid option. Please try again.\n"""
            )
            play_game = False


if __name__ == "__main__":
    # Allows the user to input their own name and country to play the game
    while True:
        player_name = input(f"\n{Fore.CYAN}NAME:\n>>> ").strip().upper()
        if len(player_name) == 0:
            print(f"{Fore.RED}This is not a valid name!")
            continue
        else:
            break
    while True:
        player_country = input(f"{Fore.CYAN}YOUR COUNTRY:\n>>> ").strip().upper()
        if len(player_country) == 0:
            print(f"{Fore.RED}This is not a valid country!")
            continue
        else:
            break
    print(
        f"""{Fore.YELLOW}\n\t
    HELLO {player_name}, WELCOME TO THE HANGMAN GAME!\n"""
    )
    print(f"{Fore.BLUE}{game_info[0]}")
    input(
        f"""\n{Fore.CYAN}
    {player_name}, PRESS ANY KEY TO START THE GAME.\n    >>> """
    )

    main()
