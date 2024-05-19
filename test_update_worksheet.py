# Import
import datetime
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, init

# Setup för Colorama
init(autoreset=True)

# Const
EXTRA_SCORE = 200
FULLY_WORD_SCORE = 500

# Getting today's date
date = datetime.datetime.today()
date = str(datetime.date.today())

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


# Test function with test case
def test_update_worksheet():
    name = "WORST PLAYER EVER"
    score = 0
    country = "NORWAY"
    update_worksheet(name, score, country)


# Run test
if __name__ == "__main__":
    test_update_worksheet()
