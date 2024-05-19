import random

words = [
    "Elliot",
    "Steven",
    "Drew",
    "Alien",
    "Classic",
    "Phone",
    "Amblin",
    "Bicycle",
    "Emotion",
    "Adventure",
    "Racoon",
    "Gertie",
    "Mary",
    "Keys",
    "Imagination",
    "Alienation",
    "Spaceship",
    "Halloween",
    "Flying",
    "Hoodie",
    "Telepathy",
    "Friendship",
    "Home",
    "Heartlight",
    "Forest",
    "Suburbia",
    "Spielberg",
    "Universal",
    "Effects",
    "John",
    "Fiction",
    "Extraterrestrial",
    "Lost",
    "Uplifting",
    "Iconic",
    "Symbiosis",
    "Escape",
    "Beam",
    "Communication",
    "Childhood",
    "Moon",
    "Stars",
    "Outsider",
    "Fear",
    "Homecoming",
    "Wonder",
]


def get_word():
    """
    Get a random word from the words list
    """
    random_word = random.choice(words)
    return random_word.upper()
