#display an integer reverse
#display integer in reverse order

def reverse(number):
    reverse = 0    
    while number > 0: #this I took from GOOGLE
        endDigit = number % 10
        reverse = (reverse*10) + endDigit
        number = number // 10
    return reverse
def main():
    number = eval(input("Please enter a number to reverse "))
    a=reverse(number)
    print (a)
main()
