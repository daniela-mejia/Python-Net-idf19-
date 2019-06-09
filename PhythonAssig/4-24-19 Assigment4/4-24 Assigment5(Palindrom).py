#Return the reversal of an integer in hexa, eg. reverse (456) returns 654
def reverse(number):
    reverse = 0    
    while number > 0: #this I took from GOOGLE
        endDigit = number % 10
        reverse = (reverse*10) + endDigit
        number = number // 10

def isPalindrome(number):
    reverse(number)
    uno = number    
    if uno == reverse:
        print("yep, it's a Palindrome")
    else:
        print("Not a Palindrome...Try again")

def main():
    number = eval(input("Please enter a number to check if Palindrome: "))
    isPalindrome(number)
main()
