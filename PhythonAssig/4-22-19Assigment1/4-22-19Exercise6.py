minutes = int(input("Enter the number of minutes: "))
MINUTES = minutes
days = 0
years = 0
while( minutes >= 1440):
    minutes -= 1440
    days += 1
while( days >= 365):
    days -= 365
    years += 1
print("%d minutes is %d years, %d days, and %d minutes" %(MINUTES,years,days,minutes))
