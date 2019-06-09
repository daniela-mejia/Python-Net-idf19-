def main():

        numMonth = 12

        months = [0] * numMonth
        whatMonths = ['Jan', 'Feb', 'Mar', 'May', 'Apr', 'May', 'Jun', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        
        def total(months):
            total = 0

            for l in months:
                total += num
            return total


        for i in range(whatMonths):
            print("enter rain amount in")
            months[i] = input(str(i+1) + ": ")
        print ("Total months is ", total(months))


        avarage = float(total(months)) / float(num_months)
        print( 'The avarage rainfall is', avarage, 'mm.')

        months.sort()
        print ('Lowest is', months[0])
        print ('Most is', months[11])
    
main ()
