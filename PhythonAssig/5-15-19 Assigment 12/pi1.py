def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = (10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x)
        else:
            q, r, t, k, m, x = (q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2)

digits = make_pi()
pi_list = []
my_array = []
for i in digits:
    my_array.append(str())
big_string = "".join(my_array)

#Each date object stores a single
#month/day such as Sep 19
#This Class ignores leap years 

class Date:
    #Constructs a date with 
    #the given month and day
    def __init__(self, m ,d):
        self._month = m 
        self._day = d

        #return the date's day
        def get_day(self)
            return _day
        def get_month(self)
            return _month
        #Returns the number of days
        #in this date's month 
        def days_in_month (self)
            count = 0
            for count in _day
                count += 1

            return _day
        def next_day()

    def compare()