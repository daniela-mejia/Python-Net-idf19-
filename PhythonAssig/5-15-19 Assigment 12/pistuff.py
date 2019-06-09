def pi_generate():
    """generator to approximate pi"""
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = (10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x)
        else:
            q, r, t, k, m, x = (q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2)


n = 1000
digits = pi_generate()
# build a list of characters, the leading 3 and n decimals
pi_list = []
for i in range(n):
    pi_list.append(str(digits.next()))
# insert the missing period at index 1 (after the 3)    
pi_list.insert(1, '.')
#print pi_list  # test
# convert the list of characters to a string
pi_str = "".join(pi_list)
print ("pi approximated to %d decimals (below it is the official pi):" % n)
print (pi_str)

