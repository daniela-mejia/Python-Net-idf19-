#This program input the number of packages, out put diacount and total
def main():
    x=99
    numPack= int(input(" Place enter the amount of packages purchased: "))
    
    if 10>= numPack <=19 :
        price= (x * numPack) * 0.20
        
    elif 20>= numPack <=49 :
        price=(x * numPack) * 0.30
        
    elif 50>= numPack <=99 :
        price=(x * numPack) * 0.40
       
    elif numPack>= 100 :
        price=(x * numPack) * 0.50
        
    else:
        price = 0
        
    total = numPack * x - price
    print(" Discount is : ", format(price, '.2f'))
    print("Your Total : ", format(total, '.2f'))
main()
