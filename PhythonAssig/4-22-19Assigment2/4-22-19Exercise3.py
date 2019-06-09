#This program input distance in km to miles
def kilometersToMiles( num ):
    num *= .6214
    return num

def main():
    num = float(input("Enter a Distance in Kilometers: "))
    num = kilometersToMiles( num )
    print("That Distance in Miles is: %.2f" %(num))

main()
