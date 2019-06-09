#Write code that does the following: opens the number_list.txt file that was createdby the code you wrote in the previous question , 
#reads all of the numbers from the file and displays them, and then closes the file

f = open ("number_list.txt")
txt = f.read()
print(txt)
f.close()


