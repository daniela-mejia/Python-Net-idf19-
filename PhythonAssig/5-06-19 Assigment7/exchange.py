#Write a program that requests the name of a county as input and then displays the nameof its currency and its exchange rate
#Daniela Mejia

def main ():
    a = 0
    fpt = open("Exchrate.txt", "r")
    country = input("Enter the country coin: ")
  
    for line in fpt:
        line = line.strip()
        data = line.split(',')
        data[0] = data[0].lower()
        if data[0] == country:
            print("Currency:",data[1],"\nExchange rate in US Dollars:",data[2])
            a+=1
        else:
            continue
    if (a == 0):
        print("Enter a country on the list next time, bud\n")
    input('')

main()