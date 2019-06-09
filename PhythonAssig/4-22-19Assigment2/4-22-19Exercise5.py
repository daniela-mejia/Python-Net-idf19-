# This program prnt county, state and total taxes
def stateTax( num ):
    return num * .04

def countyTax( num ):
    return num * .02

def main():
    sales = float(input("Enter a Month of Sales: "))
    print("County Taxes: %.2f" %(countyTax(sales)))
    print("State Taxes:  %.2f" %(stateTax(sales)))
    print("Total Taxes:  %.2f" %(countyTax(sales) + stateTax(sales)))
    print("Net Sales:    %.2f" %(sales - (countyTax(sales) + stateTax(sales))))


main()
