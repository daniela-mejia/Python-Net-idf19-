#Write a program to make change for an amount of money from 0 through99 cents input by the user
#The output of the program should show the number of coins from each denomination used to make the change.
#Daniela Mejia
       

def main ():

    coin = int(input('write the amount of money from 0 to 99 cents you need: '))

    if (coin > 100) : 
        print("WRONG TYPE A RIGHT VARIABLE")
        quit ()
    elif (coin < 100) :
        print(coin//25, "quarters")
        coin = coin%25
        print(coin//10, "dimes")
        coin = coin%10
        print(coin//5, "nickles")
        coin = coin%5
        print(coin//1, "pennies")  

main ()

