# Imports
from et_hangman_art import stages  # Importer stages


def display_hangman(attempts):
    """
    Display hangman stages from the start of the game
    and change anytime the player doesn't guess the right letter
    """
    return stages[attempts]


# Test function
def test_display_hangman():
    for i in range(len(stages)):
        print(f"Testing with {i} attempts:")
        print(display_hangman(i))
        print("\n")


# Run test
if __name__ == "__main__":
    test_display_hangman()
