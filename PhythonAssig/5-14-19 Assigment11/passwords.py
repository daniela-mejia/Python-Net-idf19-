#Write a function impose certain rules for passwords


password = str(input("Enter in a password to be checked: "))

def valid_password_checker(password):

    from string import ascii_lowercase as alphabet

    digits = '0123456789'  # creates a string of digits
    digit = 0  # acc for digits
    length = 0 # acc for length

    for char in password:  # calls on each character in string
        if char in alphabet:
            length += 1
        if char in digits:
            digit += 1
            if digit >= 2:
                flag = True
                if length >= 8 and digit is True:
                    print("valid password")
                else:
                    print("Password does not contain enough characters or digits.")
            else:
                print("Password does not contain enough digits.")

valid_password_checker(password)



def leet_speak ():
    replacements = ( ('hacker','haxor'), ('elite','eleet'), ('a','4'), ('e','3'),
                 ('l','1'), ('o','0'), ('t','+') )
my_string = "I am an elite hacker."
new_string = my_string
for old, new in replacements:
    new_string = new_string.replace(old, new)

print ( new_string )