from datetime import date
class Date:
    
    def __init__ (self, m, d):
        pass
    def compare(date1, date2):

        if (date1 > date2):
            return -1
        elif(date1 == date2):
            return 0
        elif(date1 < date2):
            return 1


    def main():
        d1 = date(2019,9,19)
        d2 = date(2015,12,13)
        result = compare(d2, d1)
        print (" -1 - date1 fist than date2 \n 0 -  both dates the same \n 1 - date2 first than date1")
        print (" The result is : " , result )
        
    main()