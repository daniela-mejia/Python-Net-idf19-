v0,v1,t = [float(x) for x in input("Enter v0, v1, and t(Seperated by commas): ").split(',',3)]
acceleration = (v1 - v0)/t
print("The average accelearation is %.4f" %(acceleration))
