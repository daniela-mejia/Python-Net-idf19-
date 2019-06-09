#This program input weight in lb to kg and heigh from inch to cm
WeightLb= float (input (" Enter your weight in lb: "))
HeighInch= float (input (" Enter your Height in inches: "))

w = float(WeightLb * 0.45359237) 
h = float( HeighInch * 2.54)

print ("Your weight in lbs is ", w)
print ("Your height in cm is ", h)
