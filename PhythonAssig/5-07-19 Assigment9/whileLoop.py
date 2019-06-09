#Write a while loop that lets the user enter a number.
#The number should be multipliedby 10, and the result assigned to a variable named product. 
#The loop should iterate aslong as product is less than 100

def main ():
    a = int(input ("Input a number: "))
    
    while a > 0 :
        if (a <= 10):
            product = a*10
            print (product)
            a += 1
        else:
            break       
main()