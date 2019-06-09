#This program enter time cals 
def main ():

    time = int( input( "enter time to know cals burn: "))
    if time == 10:
        calBurn = time * 3.9

    elif time == 15:
        calBurn = time * 3.9
    elif time == 20:
        calBurn = time * 3.9
    elif time == 25:
        calBurn = time * 3.9
    elif time == 30:
        calBurn = time * 3.9

    else:
        print ("ERROR")

    print ("You burn in ", time ,"min you burn", calBurn, "calories")
        
          
main ()
