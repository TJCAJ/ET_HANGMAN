import colorama
from colorama import Fore

colorama.init(autoreset=True)

stages = [
    """
    """,
    # ET hangman figure torso, head, two arms and one leg
    Fore.BLUE
    + r"""
     __________________________________________
    |                                        ||
    |                          ___     ___   ||
    |                   _ -- /     \-/     \ -- _
    |                /       / - \    / - \       \
    |                \            -\/-            /
    |                  \         ------         /
    |                    * - \             / - *
    |                        --_- -_- -_/_-_-//
    |                             |   |
    |                            /     \
    |                      ------       ------
    |                    /        /            \
    |                   |   | | /               |
    |                   |   |/               /  |
    |                    \  /     -   -    /    |
    |                     \/  |     -     |     |
    |                                     /    / |
    |                                    |   / | |
    |                                     \__________/
    |
|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
    """,
    # ET hangman figure torso, head, and two arms
    Fore.RED
    + r"""
     __________________________________________
    |                                        ||
    |                          ___     ___   ||
    |                   _ -- /     \-/     \ -- _
    |                /       / - \    / - \       \
    |                \            -\/-            /
    |                  \         ------         /
    |                    * - \             / - *
    |                        --_- -_- -_/_-_-//
    |                             |   |
    |                            /     \
    |                      ------       ------
    |                    /        /            \
    |                   |    | | /              |
    |                   |    |/              /  |
    |                    \  /     -   -    /    |
    |                     \/  |     -     |     |
    |                          \          /   / |
    |                           |        |  / | |
    |
|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
    """,
    # ET hangman torso, head, and one arm
    Fore.YELLOW
    + r"""
      _________________________________________
    |                                        ||
    |                          ___     ___   ||
    |                   _ -- /     \-/     \ -- _
    |                /       / - \    / - \       \
    |                \            -\/-            /
    |                  \         ------         /
    |                    * - \             / - *
    |                        --_- -_- -_/_-_-//
    |                             |   |
    |                            /     \
    |                      ------       ------
    |                    /        /            \
    |                   |   | | /               | 
    |                   |   |/                  | 
    |                    \  /     -   -    /     
    |                     \/  |     -     |           
    |                                        
    |                                                                                                                  
    |
|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
    """,
    # ET hangman torso
    Fore.YELLOW
    + r"""
      _________________________________________
    |                                        ||
    |                          ___     ___   ||
    |                   _ -- /     \-/     \ -- _
    |                /       / - \    / - \       \
    |                \            -\/-            /
    |                  \         ------         /
    |                    * - \             / - *
    |                        --_- -_- -_/_-_-//
    |                             |   |
    |                            /     \
    |                      ------       ------
    |                    /                     \
    |                   |                       |
    |                   |                       |
    |                         \    -   -    /     
    |                         |      -     |        
    |                              
    |                                                                                    
    |
|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
    """,
    # ET hangman head
    Fore.GREEN
    + r"""
      _________________________________________
    |                                        ||
    |                          ___     ___   ||
    |                   _ -- /     \-/     \ -- _
    |                /       / - \    / - \       \
    |                \            -\/-            /
    |                  \         ------         /
    |                    * - \             / - *
    |                        --_- -_- -_/_-_-//
    |                             |   |
    |                            /     \
    |                      
    |                         
    |                   
    |                  
    |                    
    |                     
    |                                              
    |                                                  
    |               
    |
|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
    """,
    # ET hangman rope
    Fore.GREEN
    + r"""
      _________________________________________
    |                                        ||
    |                                        ||
    |                             
    |                 
    |                
    |                         
    |                 
    |                  
    |                       
    |                       
    |                      
    |                           
    |                                                     
    |                                   
    |                                                       
    |                          
    |                           
    |               
    |
|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
    """,
    # initial ET state
    Fore.GREEN
    + r"""                         
                              ___     ___   
                       _ -- /     \-/     \ -- _
                    /       / - \    / - \       \
                    \            -\/-            /
                      \         ------         /
                        * - \             / - *  
                                \     /
                                 |   |
                                /     \
                          ------       ------
                        /        /            \
                       |   | | /               |
                       |   |/               /  |
                        \  /      -   -    /   |
                         \/  |      -     |    |
                              \          /   / |
                              |         |  / | |
                  \__________/          \__________/
|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
    """,
]

hangman_logo = [
    # ET hangman logo
    Fore.GREEN
    + r"""                                           
                              :::.   .:::                    
                         +=:=-::::-*=::::-=:=+               
                       ++#%@@%*+**%@%**+*%@@@%++.            
                     =*@@@@@@@@@@@%*%@@@@@@@@@@@*-           
                   :*@@@%%@@@%##*****%#%@@@%%@@@*:          
                    =@@@:*@@@@@@%%*+*%#%%@@%@*:@@@=          
                    =@%%:=@@@@%%@#%@%#@@%@@@@-:%%%=          
                    .@%%%**%%%%*+++++++*%#%%**%#%@.          
                      #@@%@%##%*+++++++*%##%@@@@%            
                        *@@@%@@%#*****#%@@@@@@*              
                          .%@@@@%%%%%%%%@@@%.                
                             :+%@@@@@@@%+:                   
                                *@@@@@#                      
                                =%@@@%=           
                __   __         =+%@@*=                 __        __        ___ 
|  | |\ | |    /  \ /  ` |__/   :+#%%*:    |\/| \ /    |__) |__| /  \ |\ | |__  
\__/ | \| |___ \__/ \__, |  \   -=#%%+-    |  |  |     |    |  | \__/ | \| |___ 
                            ..::*%#%%%*::..                                   
               ___       .====*#%%%%%#*====:           __         ___ 
|  |  /\  |\ |  |        *=+%%****#****%%+=*     |__| /  \  |\/| |__  
|/\| /~~\ | \|  |       -**%@%*********%@%**-    |  | \__/  |  | |___                 
    """,
    # ET hangman lose game logo
    Fore.RED
    + r"""                                                                          
      __   __        __      __        ___  __   __       /
|  | |__) /  \ |\ | / _`    / _` |  | |__  /__` /__`     / 
|/\| |  \ \__/ | \| \__>    \__> \__/ |___ .__/ .__/    .  
                                               
                         =+       ___  ___      __  ___          .  __  
                         =:      |__    |      /__`  |   /\  \ / ' /__` 
                       .:+=:     |___ . |  .   .__/  |  /~~\  |    .__/                        
                    ==:   ..:===                   
                  =:    ..:-===++-                 
                 --....::--===+*##:                
                :====+=+===***##%#*-               
         .=+=-::==*+====-=-+++##%%%%**+++-         
     :*=..         ...  ..:::::----==+**###*#*.    
     **+-::. .   ...   ....::::::----==+*+*#%%+    
       =#%#*##%%#***+========+**##%%%%%##%%#-      
           .=*%%%#****************#%%%*-.          
                  =##*****+****##=                                                                                                                                                                                                                                                                                                                                                                                                       
    """,
    # ET hangman win game logo
    Fore.GREEN
    + r"""                                                                                                                                                                                                                                                             
                                             __           __     __       ___     /
                    =*-                 \ / /  \ |  |    |  \ | |  \    |  |     / 
                 @@@@#@@@@               |  \__/ \__/    |__/ | |__/    |  |    .                 
             +**=+**#*#%%=+%%            ___  ___        __                       __  
              +%@@@@%@%@@@@*            |__    |      | /__`    | |\ |    |__| | /__` 
                 =*%@@@*+:              |___ . |  .   | .__/    | | \|    |  | | .__/     
                   +#@@                  __     __   ___          __         ___     /
                   *#%%+                |__) | |  \ |__     |__| /  \  |\/| |__     / 
            **%@++*#*#%%*=@@***         |  \ | |__/ |___    |  | \__/  |  | |___   .     
     *-+-%@@@@@##@#+++++@@+@@@@@#%#++:    
   =  .:-=+**+**%@%%%%%%@@#*###%%%%%%*+=  
   ++=::--*:*--:==+++++++=-:-*-=%***###=  
     =@##*+=--::::-------::--==*###%#     
        :*@@@@@@@@@@%%%@@@@@@@@@#=        
          .++#%%@@@@@@@@@@@%%+*:          
              :-=********+=-:                                                                                                                                                                                                                         
    """,
    # ET hangman extra win game logo
    Fore.GREEN
    + r"""                          
                                :=+===+====+===+=:               
                            :++*%%*+=-=%+--+*%%%*+-             
                            =*%@%%@%%@#+++*%@%@@%@%#*            
                          :*%=#@+***#****#*+@=@*#:*#=           
                          :%%-@@@@%++*%%++-=*%@@@@=#*           
                          :*#+*@@%%%#***::-**%@@%***=           
 __   __   ___      ___     .%%+==**#@@@@@@@@:==-=*%-         __   __      /
/ _` |__) |__   /\   |        +@@@@%%*##**##%@@@%:         | /  \ |__)    / 
\__> |  \ |___ /~~\  |    *-     :-=*@@@@@@*=-:         \__/ \__/ |__)   .                         
                        =*=*=+*.     -@@@@=                            
                        .**#%*=      .@%%#-                     
                            =%#=      :@@##=                     
                              @*:  :=*%%%#**+:=                  
                              =%**+:+%*%%##*-%=*                 
       ___     ___  __         *%**%@+:=**=-=%%=+.   __   __         ___  __      /
      |__  \_/  |  |__)  /\     :@@%+****=##@@==-   |__) /  \ | |\ |  |  /__`    / 
      |___ / \  |  |  \ /~~\    #@%#*******%@@@*=:  |    \__/ | | \|  |  .__/   .                                                                                                                                                                                       
""",
]

game_info = [
    # ET hangman game rules
    Fore.CYAN
    + r"""
    _________________________________________________________________________
   |  |                ===============================                    |  |
   |  |                | |   G A M E   R U L E S   | |                    |  |
   |  |                ===============================                    |  |
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
   |  |  * 200 points if you guessed the right word                       |  |
   |  |  * 500 extra points to complete the full word with max 3 letters  |  |
   |  |    already guessed.                                               |  |
   |  |                                                                   |  |
   |  |  HINT!                                                            |  |
   |  |  * All random words have a connection to the original film.       |  |
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
