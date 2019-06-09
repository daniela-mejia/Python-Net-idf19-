
def mystery(a):
   i=0
   for i in range (len(a)-2 , 0, -1):
        if (a[i + 1] <= a[i - 1]):
            a[i] += 1
            
def main ():
    a1=42
    mystery(a1)
    print (mystery)
main()
