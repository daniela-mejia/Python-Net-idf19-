#Determine the monthly payment for a car loan.Example output
#Daniela Mejia
def main ():

    loan_Amount = float(input('Enter the amount of your loan: '))
    loan_interest = float(input('Enter the interest rate (%): '))
    loan_years = int(input('Enter the numbers of years for this loan: '))

    repayment_years = loan_years * 12
    repayment_interest = loan_interest/100
    #Formula
    #Month_payment = L[i(1+i)n] / [(1+i)n-1]
    monthlyRepay =(loan_Amount * repayment_interest * (1+repayment_interest) * repayment_years / ((1+repayment_interest) * repayment_years - 1))
    print (' You have to pay monthly : ', (monthlyRepay))
    #print (monthlyRepay)

main ()