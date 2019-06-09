num = 0.0
for i in range(5):
    string = "Please Enter Item #" + str(i + 1) + "'s Price: "
    num += float(input(string))
print("Subtotal: %.2f" %(num))
tax = num*.06
print("Sales Tax: %.2f" %(tax))
print("Total: %.2f" %(tax+num))
