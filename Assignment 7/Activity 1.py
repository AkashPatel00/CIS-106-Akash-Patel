# This program asks the user for their pay rate and amount of hours, if the user has more than 40 hours then it'll calculate in overtime
# it then calculates their weekly, monthly and annual income


def calculate_pay(hours, rate):
    pay = rate * hours
    if (hours > 40):
        pay = pay + rate * hours * 0.5
    return pay


def calculate_weekly(pay):
    weekly = pay
    return weekly


def calculate_monthly(pay):
    monthly = pay * 4
    return monthly


def calculate_annual(pay):
    annual = pay * 52
    return annual


def display_result(pay, weekly, monthly, annual):
    print("Your weekly pay is.. " + str(weekly) + "Your monthly pay is.. " + str(monthly) + "Your annual pay is.. " + str(annual))


def get_rate():
    print("Enter pay rate")
    rate = float(input())
    return rate


def get_hours():
    print("Enter hours worked")
    hours = float(input())
    return hours


def main():
    rate = get_rate()
    hours = get_hours()
    pay = calculate_pay(hours, rate)
    weekly = calculate_weekly(pay)
    monthly = calculate_monthly(pay)
    annual = calculate_annual(pay)
    display_result(pay, weekly, monthly, annual)


main()
