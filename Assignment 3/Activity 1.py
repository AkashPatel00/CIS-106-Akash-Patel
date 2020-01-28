print("Enter hours worked in a week")
hours = int(input())
print("What is your pay rate?")
rate = int(input())
pay = hours * rate
monthly = hours * rate * 4
yearly = hours * rate * 52
print("Your Weekly pay is.." + str(pay))
print("Your Monthly pay is.." + str(monthly))
print("Your Yearly pay is.." + str(yearly))
