"""This file runs the ET Hangman game."""

import datetime
import gspread
from google.oauth2.service_account import Credentials
from et_hangman_words import *
from et_hangman_art import *

import colorama
from colorama import Fore

colorama.init(autoreset=True)

# Import date from datetime
date = datetime.datetime.today()
today_date = date.strftime("%d/%m/%Y")

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("ET_Hangman_Leaderboard")

leaderboard = SHEET.worksheet("leaderboard")

data = leaderboard.get_all_values()

# CONST
CORRECT_GUESSED = 25
EXTRA_SCORE = 200
FULLY_WORD_SCORE = 500
PLAY_AGAIN_MSG = f"""{Fore.CYAN}
A - PLAY AGAIN
B - LEADERBOARD
C - EXIT THE GAME
"""
