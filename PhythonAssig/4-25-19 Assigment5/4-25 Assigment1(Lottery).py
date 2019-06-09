# Design a program that generates 7 random digit lottery number. 


import random

#Initialise an empty list that will be used to store the 6 lucky numbers!
lotNumbers = []

for i in range (0,7):
  number = random.randint(0,9)
  #Check if this number has already been picked and ...
  while number in lotNumbers:
    # ... if it has, pick a new number instead 
    number = random.randint(0,9)
  
  #Now that we have a unique number, let's append it to our list.
  lotNumbers.append(number)

#Sort the list in ascending order
lotNumbers.sort()

#Display the lsit on screen:
print("LUCKY! Lottery numbers are: ") 
print(lotNumbers)
