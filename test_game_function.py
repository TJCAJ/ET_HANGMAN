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
leaderboard = SHEET.worksheet("leaderboardd")

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
