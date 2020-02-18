# This program is designed to ask the user for any number of miles
# The program will then convert it into yards, feet and inches.

def calculateFeet(miles):
    feet = miles * 5280
    
    return feet

def calculateInches(miles):
    inches = miles * 63360
    
    return inches

def calculateYards(miles):
    yards = miles * 1760
    
    return yards

def displayResult(miles, feet, inches, yards):
    print("distance in yards.." + str(feet) + "distance in feet.." + str(inches) + "distance in inches.." + str(yards))

def getMiles():
    print("Enter amount of miles")
    miles = float(input())
    
    return miles

# Main
miles = getMiles()
yards = calculateYards(miles)
feet = calculateFeet(miles)
inches = calculateInches(miles)
displayResult(miles, yards, feet, inches)
