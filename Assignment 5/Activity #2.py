# This program asks for the users age and converts it into
# months, days, hours and seconds

def get_age():
    print("Enter how old you are:")
    age = str(input())
    return age


def calculate_months(age):
    months = (age * 12)
    return months


def calculate_days(age):
    days = (age * 365)
    return days


def calculate_hours(age):
    hours = (age * 8760)
    return hours


def calculate_seconds(age):
    seconds = (age * 31, 536, 000)
    return seconds


def display_result(months, days, hours, seconds):
    print("Your age in months is..") + str(months)
    print("Your age in days is..") + str(days)
    print("Your age in hours is..") + str(hours)
    print("Your age in seconds is..") + str(seconds)


def main():
    age = get_age()
    months = calculate_months(age)
    days = calculate_days(age)
    hours = calculate_hours(age)
    seconds = calculate_seconds(age)
    display_result(months, days, hours,seconds)


main()
