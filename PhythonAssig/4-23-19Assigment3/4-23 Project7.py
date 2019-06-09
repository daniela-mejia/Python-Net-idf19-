#This program in while loops if x< 100 multiply by 10, if your choice is 1 
#then add first and second input number then if i is in range to 101 then 
#print 100 or else number  times 10
def main():

    x = 0
    while x < 100:
       product = float(input(" enter a number: "))
       x = product * 10
       print(" product = %.2f" %(x))
       break
    
    choice = 1
    while choice == 1:
        a = float(input(" Enter First Number = "))
        b = float(input (" Enter Second Number = "))
        sumNum = a + b
        print("Sum of two numbers= ", sumNum)
        choice = int(input("Press one to repeat the operation: "))

    for i in range (101):
        if i == 100:
            print (100)
        else:
            print ( i*10, end= ', ')
                     
main()
