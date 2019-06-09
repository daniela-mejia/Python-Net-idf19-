#Write a program reads content of two text files and cmpares them

def main():
    words1= False

    findwords1 = input ("Write the girl's name? ")

    #open file numero uno

    girl_name = open('GirlNames.txt', 'r')

    #read the first item in the list
    searchGirl = girl_name.readline()

    #Read the rest of the file
    while searchGirl != '':

        #Strip names from space(\n)
        searchGirl = searchGirl.rstrip('\n')

        #determine whether this item matches the search 
        if searchGirl == findGirl:
            print(findGirl, 'is found in the top names for girls')
            print('')
            foundGirl =  True
        
        
        searchGirl = girl_name.readline()
    #create the boy 

    foundBoy = False

    findBoy = input("Write the name of the boy?")

    boy_name = open('BoyNames.txt','r')

    searchBoy = boy_name.readline()

    while searchBoy != '':
        searchBoy = searchBoy.rstrip('\n')

        if searchBoy == findBoy:
            print(findBoy,'is found in the top names for boys')
            print('')
            foundBoy = True
        
        searchBoy = boy_name.readline()
    
    girl_name.close()
    boy_name.close()

    if not foundGirl:
            print('The name was not in the list of girls')
    if not foundBoy:
            print('The name was not in the list of boys')
main()