# Import
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, init

# Setup for Colorama
init(autoreset=True)

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


# Test function
def test_display_leaderboard():
    display_leaderboard()


# Run test
if __name__ == "__main__":
    test_display_leaderboard()
