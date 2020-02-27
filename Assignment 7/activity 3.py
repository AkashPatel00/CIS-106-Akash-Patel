# Program asks user for amount in miles then asks to convert into US measurements or Metric then converts


def get_miles(scale):
    print("Enter" + scale + "miles:")
    miles = float(input())
    return miles


def get_choice():
    print("Enter U if you want to convert into US or M if you want to convert into Metric:")
    choice = input()
    return choice


def process_us():
    miles = get_miles("US")
    calculate_us(miles)


def process_metric():
    miles = get_miles("Metric")
    calculate_metric(miles)

def calculate_us(miles):
    yards = (miles * 1760)
    feet = (miles * 5280)
    inches = (miles * 63380)
    print (str(miles) + " miles, " + str(yards) + " yards, " + str(feet) + " feet, " + str(inches) + " inches.")


def calculate_metric(miles):
    kilometers = (miles * 1.60934)
    meters = (miles * 1609.34)
    centimeters = (miles * 160934)
    print(str(miles) + "miles," + str(kilometers) + "kilometers," + str(meters) + "meters," + str(centimeters) + "centimeters.")


choice = get_choice()
if choice == "U" or choice == "u":
    process_us()
elif choice == "M" or choice == "m":
    process_metric()
else:
    print("You must insert U or M to convert your miles")

#Main
miles = get_miles()
choice = get_choice()
yards = calculate_us(miles)
feet = calculate_us(miles)
inches = calculate_us(miles)
kilometers = calculate_metric(miles)
meters = calculate_metric(miles)



