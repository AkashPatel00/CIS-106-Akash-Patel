# Program asks user for amount in miles then asks to convert into US measurements or Metric then converts


def get_miles():
    print("Enter miles:")
    miles = float(input())
    return miles


def get_choice():
    print("Enter U if you want to convert into US or M if you want to convert into Metric:")
    choice = input()
    return choice


def process_us(miles):
    yards = calculate_yards(miles)
    feet = calculate_feet(miles)
    inches = calculate_inches(miles)
    display_us(miles, yards, feet, inches)


def process_metric(miles):
    kilometers = calculate_kilometers(miles)
    meters = calculate_kilometers(miles)
    centimeters = calculate_kilometers(miles)
    display_metric(miles, kilometers, meters, centimeters)


def calculate_yards(miles):
    yards = miles * 1760
    return yards


def calculate_feet(miles):
    feet = miles * 5280
    return feet


def calculate_inches(miles):
    inches = miles * 63380
    return inches


def display_us(miles, yards, feet, inches):
    print (str(miles) + " miles, " + 
        str(yards) + " yards, " + 
        str(feet) + " feet, " + 
        str(inches) + " inches.")


def calculate_kilometers(miles):
    kilometers = (miles * 1.60934)
    return kilometers


def calculate_meters(miles):
    meters = (miles * 1609.34)
    return meters


def calculate_centimeters(miles):
    centimeters = (miles * 160934)
    return centimeters


def display_metric(miles, kilometers, meters, centimeters):
    print(str(miles) + " miles, " + 
        str(kilometers) + " kilometers, " + 
        str(meters) + " meters, " + 
        str(centimeters) + " centimeters.")


def main():
    miles = get_miles()

    choice = get_choice()
    if choice == "U" or choice == "u":
        process_us(miles)
    elif choice == "M" or choice == "m":
        process_metric(miles)
    else:
        print("You must insert U or M to convert your miles")


main()
