# The purpose of this program is to be able to convert miles to yards, 
# feet and inches.

print("Enter amount of miles")
miles = int(input())

yards = miles * 1760
feet = miles * 5280
inches= miles * 63360

print("Your distance in yards is.." + str(yards))
print("Your distance in feet is.." + str(feet))
print("Your distance in inches is.." + str(inches))
