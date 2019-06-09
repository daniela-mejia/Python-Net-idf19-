import random
from time import sleep



ListofWord = ("DOG", "CAT")
word = random.choice(ListofWord)
positive_saying("awesome", "keep guessing")
Max_Wrong = len(word) - 1
so_far = ("*") * len(word)
used = []
wrong = 0

print("\t \t Welcome to Hangman!")
print(' ')
input("Enter to Start")

while wrong < Max_Wrong and so_far != word:
    print(Hangman[wrong])
    print("You got right: ", so_far)
    print("Letters used: ",used)

    guess = input ("Guess a letter: ").upper()
    sleep(1)
    print()

    while guess in used:
        print("Try again... You used that letter already")
        guess = input ("Guess a letter: ").upper()
        sleep(1)
        print()
    used.append(guess)
    if guess in used:
        print(random.choice(positive_saying),"...Updating word so far")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("INCORRECT!! Try Again")
        wrong += 1
print ("Calculating result..")
sleep(1)
if wrong == Max_Wrong:
    print("YOU SUCK! Better luck next time")
else:
    print("WINNER! Congratulations!")

print()
input("Press Enter to leave: ")

    
