class Account:
    # Construct an Account object 
    __balance = 0.0
    def __init__(self, id, balance=100):
        self.__id = id
        self.__balance = balance
        

    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def withdraw(self, amount):
        
        if amount <= self.__balance: 
            self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount
        


def main():

    idNum = int(input ("Welcome what is your ID number: "))
    acc = Account(idNum)
    # Create an account with width 4 and height 40 
    
    loop = True

    while loop == True:
        print("Welcome to ATM what do you want to do\n ---")
        options = int (input ("Here are your options: \n 1) Current Balance \n 2) Withdrawing \n 3) Deposit \n 4) Main menu \n 5) Exit \n --------------> "))

        if idNum in range (0,10) :
            print("ID is correct you can continue", acc.getId())
            if options == 1:
                print("ID is", acc.getId())
                print("Balance is ", acc.getBalance())
                print (' ')
                continue
            elif options == 2:
                amount =  int(input("How much would you like to Withdraw? "))
                acc.withdraw(amount)
                print(" -----------New Balance after withdraw is =", acc.getBalance()) 
                print(' ')
                continue
            elif options == 3:
                amount =  int(input("How much would you like to Deposit? "))
                acc.deposit(amount)
                print(" -----------New Balance after deposit is =", acc.getBalance()) 
                print(' ')
                continue
            elif options == 4:
                print ("To Main Menu! \n")
                continue
            elif options == 5:
                print ("Have a good day! \n")
                break
        else:
            print("Wrong account Number. Try again ")
            break
          
main()
