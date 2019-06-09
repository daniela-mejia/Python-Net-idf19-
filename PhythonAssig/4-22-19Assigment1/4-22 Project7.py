#This program gives you the accelatation inputing star velocity, ending velocity and time
vo = float(input (" Input your Starting Velocity vo: "))
v1 = float(input (" Input your Ending Velocity v1: "))
t = float(input (" Input your time: "))

accl = (v1-vo)/t

print(" Average Acceleration is %.5f" %(accl))
