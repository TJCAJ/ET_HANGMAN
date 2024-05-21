# Display the hangman stages
def display_hangman(attempts):
    """
    Display the hangman stages during the game
    """
    return stages[attempts]


# Display the players score
def display_score(score):
    """
    Displays the players score in the game
    """
    print(f"\tSCORE: {score}")


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
