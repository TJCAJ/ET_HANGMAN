import random

words = [
    "Elliot",
    "Steven",
    "Drew",
    "Alien",
    "Hollywood",
    "Phone",
    "Amblin",
    "Bicycle",
    "Reesespieces",
    "Strangerthings",
    "Racoon"
]


def get_word():
    """
    Get a random word from the words list
    """
    random_word = random.choice(words)
    return random_word.upper()