# the function should accept an argument and display the productof its multiply
#by ten

def main():
    time= int(input(" Input a number that will be multiply by 10= "))
    times_ten(time)
    
def times_ten (diez):
    result= diez*10
    print("number by 10 is = %d" %(diez))
    show_value(12)

def show_value(quantity):
    print(quantity)

main()
    
