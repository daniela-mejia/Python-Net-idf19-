import sys
from math import pi

def calcPi():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4*q+r-t < n*t:
            yield n
            nr = 10*(r-n*t)
            n  = ((10*(3*q+r))//t)-10*n
            q  *= 10
            r  = nr
        else:
            nr = (2*q+r)*l

            nn = (q*(7*k)+2+(r*l))//(t*l)
            q  *= k
            t  *= l
            l  += 2
            k += 1
            n  = nn
            r  = nr



number_of_places =str(input("Enter the number of decimal places you want to see: "))
fraser = calcPi()
length_of_pi = [fraser]
for number_of_places in fraser:
    length_of_pi.append(str(number_of_places))

print("".join(length_of_pi))