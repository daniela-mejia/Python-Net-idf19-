import random
from time import sleep

HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

ListofWords = ("DOG", "CAT", "DONKEY")
word = random.choice(ListofWords)
POSITIVE_SAYINGS = ("Use your brain", "Awesome")
MAX_WRONG = len(word) - 1
so_far = ("*") * len(word)
used = []
wrong = 0

print("\t \t Welcome to Hangman !")
print()
input("Press Enter to START: ")

while wrong < MAX_WRONG and so_far != word:
    #format for hangman game 
    print()
    print(HANGMAN[wrong])
    print("You got right: ", so_far)
    print("Letters used: ", used)

    guess = input("Guess a letter: ").upper()
    sleep(1) # Time delay - allows userfriendly reading
    print()

    while guess in used:
        print("Try again... You've already used this letter")
        guess = input("Guess a letter: ").upper()
        sleep(1)
        print()
    used.append(guess)

    if guess in word:
        print(random.choice(POSITIVE_SAYINGS),"...Updating word so far...")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess

            else:
                new += so_far[i]
        so_far = new 

    else:
        print("INCORRECT! Try again!")
        wrong += 1

print("Calculating result...")
sleep(1)
if wrong == MAX_WRONG:
    print("YOU SUCK! Better luck next time!")

else:
    print("WINNER! Congratulations!")

print()
print()
input("Press Enter to Leave: ")