 #Start by declaring your functions:
def isEven(n):
    return n % 2 == 0

def countEven():
    count = 0
    str_of_Num = input("Please enter numbers separated by spaces: ")
    list_of_num = str_of_Num.split(' ')
    for number in list_of_num:
        number_as_int = int(number)
        if isEven(number_as_int) == True:
            count += 1
    print("There are " + str(count) + " even numbers.")
countEven()    