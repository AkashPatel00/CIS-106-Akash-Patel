def get_choice():
    print("Enter U if you want to convert into US or M if you want to convert into Metric:")
    choice = input()
    return choice


def process_US():
    miles = get_miles("US")
    yards = calculate_us
    feet = calculate_us
    inches = calculate_us
    result = calculate_us(miles)
    display_result("US", miles, result, "Metric", yards, feet, inches)


def process_Metric():
    miles = get_miles("Metric")
    kilometers = calculate_metric
    meters = calculate_metric
    centimeters = calculate_metric
    result = calculate_metric(miles)
    display_result("Metric", miles, result, "US", kilometers, meters, centimeters)


def get_miles(scale):
    print("Enter" + scale + "miles:")
    miles = float(input())
    return miles


def calculate_us(miles):
    yards = (miles * 1760)
    feet = (miles * 5280)
    inches = (miles * 63380)
    return (yards, miles, feet, inches)


def calculate_metric(miles):
    kilometers = (miles * 1.60934)
    meters = (miles * 1609.34)
    centimeters = (miles * 160934)
    return (kilometers, meters, centimeters)


def display_result(miles, fromScale, result, toScale):
    print(str(miles) + fromScale + str(result) + toScale)


def main():
    choice = get_choice()
    if choice == "U" or choice == "u":
        process_US()
    elif choice == "M" or choice == "m":
        process_Metric()
    else:
        print("You must insert U or M to convert your miles")
