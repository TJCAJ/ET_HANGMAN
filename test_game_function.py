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


def display_hangman(attempts):
    """
    Displays hangman stages from start of the game
    and changes when the player doesn't guess the right letter
    """
    return stages[attempts]


def word_space(full_word):
    """
    Add space in between letters in the random word
    """
    for i in full_word:
        print(i, end=" ")
    print()  # Adds a new line


def display_score(score):
    """
    Displays the players score in the game
    """
    print(f"\tSCORE: {score}")


def update_worksheet(name, score, country):
    """
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
    print(f"{Fore.YELLOW}\n\tLET'S HELP E.T. HOME!\n")
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
                {guess} IS NOT IN THE WORD. E.T. DOESN'T KNOW EITHER!\n"""
                )
                attempts -= 1
                guessed_letters.append(guess)
                guessed_wrong.append(guess)
            else:
                print(
                    f"""{Fore.GREEN}\n\t
                GREAT, {guess} IS IN THE WORD! E.T IS ON THE WAY!\n"""
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
                print(
                    f"{Fore.RED}\n\t{guess}, IS NOT THE WORD. E.T. IS GETTING WORRIED. TRY AGAIN!"
                )
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


def final_result(guessed, random_word, guessed_right, score):
    """
    Check if the player loses or won the game guessing the word letter
    by letter or the word at once
    """
    if guessed and len(random_word) >= 6 and guessed_right <= 3:
        print(f"{Fore.GREEN}{hangman_logo[3]}")
        print(
            f"""{Fore.GREEN}
        YOU WIN {player_name}, E.T IS BLOWN AWAY! YOU HAVE GUESSED THE WORD COMPLETELY AT ONCE!\n
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
    update_worksheet(player_name, score, player_city)
    display_score(score)


# Test function for the game
def test_game_function():
    """
    Test the game function with a predefined word.

    Preconditions:
    - The word 'SPIELBERG' is used for testing.

    This function does not return any value. It made to verify the game logic.
    """
    random_word = "SPIELBERG"
    game(random_word)


# Run test
if __name__ == "__main__":
    test_game_function()
