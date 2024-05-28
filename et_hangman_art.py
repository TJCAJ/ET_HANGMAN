import colorama
from colorama import Fore

colorama.init(autoreset=True)

stages = [
    """
    """,
    # ET hangman figure torso, head, two arms and one leg
    Fore.BLUE
    + r"""
    __________________
    |               ||
    |        :=+=+=.||
    |       **%: -%+#
    |          =#- _//
    |      /&:*: -+-%\
    |     |  ## :.#+  |
    |        :*=*=+:
    |        :*+++*.:.=*
    |____________________
    """,
    # ET hangman figure torso, head, and two arms
    Fore.RED
    + r"""
    __________________
    |               ||
    |        :=+=+=.||
    |       **%: -%+#
    |          =#- _//
    |          =#- -/
    |      /&:*: -+-%\
    |     |  ## :.#+  |
    |        :*=*=+:
    |____________________
    """,
    # ET hangman torso, head, and one arm
    Fore.YELLOW
    + r"""
    __________________
    |               ||
    |        :=+=+=.||
    |       **%: -%+#
    |          =#- _//
    |          =#- -/
    |      /&:*: -+-%\
    |        ## :.#+  |
    |        :*=*=+:
    |____________________
    """,
    # ET hangman torso
    Fore.YELLOW
    + r"""
    __________________
    |               ||
    |        :=+=+=.||
    |       **%: -%+#
    |          =#- _//
    |          =#- -/
    |      /&:*: -+-%\
    |        =%. :%:
    |        ## :.#+
    |____________________
    """,
    # ET hangman head
    Fore.GREEN
    + r"""
    __________________
    |               ||
    |        :=+=+=.||
    |       **%: -%+#
    |       *+*. :#=*
    |          =#- _//
    |          =#- -/
    |          =#-
    |
    |____________________
    """,
    # ET hangman rope
    Fore.GREEN
    + r"""
    __________________
    |               ||
    |               ||
    |              _//
    |              -/
    |
    |
    |
    |____________________
    """,
    # initial ET state
    Fore.GREEN
    + r"""
             :=+=+=.
            **%: -%+#
               =#-
           /&:*: -+-%\
          |  ## :.#+  |
             :*=*=+:
         *=:::*+++*.:.=*
      _____________________
    """,
]

hangman_logo = [
    # ET hangman logo
    Fore.GREEN
    + r"""
           .::-:::-::.
        ==*#*==+#+==*#*=+
       +%*#%%##+=+##%%%*%+
          :###*****##%:
             :#@%@#:      | | ._  |  _   _ |    ._ _       ._  |_   _  ._   _
              :#%#-       |_| | | | (_) (_ |<   | | | \/   |_) | | (_) | | (/_
              :=*+:       _  ___                      /    |
              :=*+:      |_   |           _. ._ _|_  _   |_   _  ._ _   _  |
           :--+***+--:   |_ o | o   \/\/ (_| | | |_ _>   | | (_) | | | (/_ o
          ==++==+==++==
    """,
    # ET hangman lose game logo
    Fore.RED
    + r"""
            ::.-:.-. =
           -*##--:.##*-   \    / ._ _  ._   _     _       _   _  _
           --*--   +=-=    \/\/  | (_) | | (_|   (_| |_| (/_ _> _>
             --+=---:        _  ___         _|    _|
             .  -#. :       |_   |      _ _|_  _.     _ |
                --          |_ o | o   _>  |_ (_| \/ _> o
             . :..:                               /
        .::-=**=+##+--:::.
    """,
    # ET hangman win game logo
    Fore.GREEN
    + r"""
                  .+
              .+..:::-=*.             \_/ _         _| o  _|   o _|_ |
             =:..::-===++-             | (_) |_|   (_| | (_|   |  |_ o
     :==-::.:--=====++********++=.      _  ___
   :+=:.....:::..:::::-----==+=+*#*    |_   |     o  _   o ._    |_  o  _
    .****###**++==+=++**####***+.      |_ o | o   | _>   | | |   | | | _>
 __   _   _   ._   _  o ._ _|_  _      ._ o  _|  _    |_   _  ._ _   _  |
  _| |_  / \  |_) (_) | | | |_ _>      |  | (_| (/_   | | (_) | | | (/_ o
 __| __/ \_/  |
    """,
    # ET hangman extra win game logo
    Fore.GREEN
    + r"""
            .-====--:+::-==-=-.
          .**+@@%*+*+*--=*%@@+**     __
           -*+=+++%#*#=+%==+=+*-    /__ ._ _   _. _|_    o  _  |_  |
            .-%%#%*+**+++##%%-.     \_| | (/_ (_|  |_    | (_) |_) o
         .*= ::...-%%%%@=....              __  _   _    _|
        .*+*+*:.   .#%#+.                   / / \ / \
         ..***.    .#%*+.                  /  \_/ \_/
            :#+..==*##**+=:       _    _|_ ._ _.   ._   _  o ._ _|_  _ |
             .=++%*-=++==*#=+.   (/_ >< |_ | (_|   |_) (_) | | | |_ _> o
            ....*#**+++***%%+=..                   |
""",
]

game_info = [
    # ET hangman game rules
    Fore.CYAN
    + r"""
    _________________________________________________________________________
   |  \                      G A M E   R U L E S                          /  |
   |  |                                                                   |  |
   |  |  1 - You have 7 attempts to try to find the right password for    |  |
   |  |      E:T.s phone by inputting letters or the full word.           |  |
   |  |      If you succeed E.T. can make his call and go home.           |  |
   |  |                                                                   |  |
   |  |  2 - If you guess a wrong letter you will lose an attempt and the |  |
   |  |      E.T. hangman will begin building.                            |  |
   |  |                                                                   |  |
   |  |  3 - When you reach 0 attempts E.T. can't phone home and has to   |  |
   |  |      stay on earth forever. Game Over                             |  |
   |  |                                                                   |  |
   |  |  POINTS:                                                          |  |
   |  |  * 25 points per letter guessed right                             |  |
   |  |  * 300 points if you guessed the right word                       |  |
   |  |  * 700 extra points to complete the full word with max 3 letters  |  |
   |  |    already guessed.                                               |  |
   |  |                                                                   |  |
   |  /  HINT! All random words have a connection to the original film.   \  |
   |_________________________________________________________________________|
    """,
    # ET hangman leaderboard
    Fore.YELLOW
    + r"""
    ============================================================

                      L E A D E R B O A R D

    ============================================================
    \tPOS\tNAME\t SCORE\t  DATE\t\tCOUNTRY
    ============================================================
    """,
]
