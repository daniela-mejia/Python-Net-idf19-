weight = float(input("Enter weight in pounds: "))
height = float(input("Enter height in inches: "))
weight *= .45359237
height *= .0254
bmi = weight/(height ** 2)
print("BMI is %.4f" %(bmi))
