#This program display total and each price of items
#purchase 5 items and ask for the price of each item
subtotal = 0.0

for n in range(5):
    x = "item " + str(n+1) + " cost: "
    subtotal += float(input(x))
#display the subtotal sale
  
print("Subtotal= %.2f " %(subtotal))

#tax amount by 6%
tax = subtotal *0.6
print("Tax= %.2f" % (tax))

total = subtotal + tax
print("Total= %.2f" % (total))
