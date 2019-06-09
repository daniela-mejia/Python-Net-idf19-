#This program has different functions for the amount of  
#fat and carbs you eat a day
def calFromFat( num ):
    return num * 9

def calFromCarbs( num ):
    return num * 4

def main():
    fat = int(input("Enter the Number of Grams of Fat: "))
    carbs = int(input("Enter the Number of Grams of Carbs: "))
    print("Calories from Fat: %.2f" %(calFromFat(fat)))
    print("Calories from Carbs: %.2f" %(calFromCarbs(carbs)))

main()
