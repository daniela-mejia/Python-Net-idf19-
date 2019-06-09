# This Program finds how many even numbers are in the input number by the user
# Start defining a function 
def Even(a):
    return a % 2 == 0
def countEven():
    count = 0
    string_of_Num = int(input("Please enter a numbers separated by spaces: "))
    list_of_Num = string_of_Num.split(' ')
    for number in list_of_Num:
        num = int(number)
        if Even(num) == True:
            count += 1
        print ("There are" + str (count) + "even numbers.") 
