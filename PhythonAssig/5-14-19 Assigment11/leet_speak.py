with open("words.txt", "a+") as myfile:
    leet = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 'A': '4', 'E': '3', 'I': '1', 'O': '0'}
    myfile.write(leet)
    
data = string.replace(leet)

for k, v in leet.items(): #iterating through dictionary (not string)
    s = string.replace(k, v)
    
string.close()   

print(s)