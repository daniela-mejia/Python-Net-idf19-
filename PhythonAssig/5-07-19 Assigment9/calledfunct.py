# The following statement calls a function named half, which returns a value that is halfthat of the argument. 
# (Assume the number variable references a float value.)Writecode for the function

def half(num):
    return num/2

def main ():
    a = int(input("Write a number: "))
    result = half (a)
    print ("Your number ini half is: ", result)
main()
