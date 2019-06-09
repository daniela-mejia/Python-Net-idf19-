# write a funtion that checks whether two words are anagrams.

def isAnagram (s1,s2):

    alist = list(s2)

    right1 = 0
    stillOK = True

    while right1 < len(s1) and stillOK:
        right2 = 0
        found = False
        while right2 < len(alist) and not found:
            if s1[right1] == alist[right2]:
                found = True
            else:
                 right2 += 1

        if found:
            alist[right2] = None
        else:
            stillOK = False

        right1 += 1

    return stillOK
def main ():

    print ("Check if words are Anagram")
    Uno = str(input("Write your first word: \n"))
    Dos = str(input("Write your second word: \n"))
    print ("Anagram?................")
    print(isAnagram(Uno,Dos))
main()