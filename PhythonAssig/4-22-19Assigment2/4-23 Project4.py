#ask number of fat grams and carbohydrate grams daily to get cal from them

fat= float(input("fat in grams you eat in a day: "))
carbohydrate= float(input("carbohydrates grams you eat in a day: "))

calFat= fat*9
calCarb= carbohydrate*4

print(" this is the amount of cals of Fat you eat in a day: %.2f " %(calFat))
print(" this is the amount of cals of Carbohydrates you eat in a day: %.2f" %(calCarb))
