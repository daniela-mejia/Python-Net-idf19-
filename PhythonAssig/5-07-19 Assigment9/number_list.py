#Write code that does the following: opens an output file with the file namenumber_list.txt, 
#uses a loop to write the numbers 1 through 100 to the file, and thencloses the file.

for i in range(1,100):
    f = open ("number_list.txt","w")
    f.write("This line%d\r\n" %(i+1))
    
    f.close()



