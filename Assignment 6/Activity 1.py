# This program asks the user for their pay rate and amount of hours
# it then calculates their weekly, monthly and annual income


def calculatePay(hours, rate):
    pay = rate * hours

    return pay


def calculateWeekly(pay):
    weekly = pay * 7

    return weekly


def calculateMonthly(pay):
    monthly = pay * 30

    return monthly


def calculateAnnual(pay):
    annual = pay * 365

    return annual


def displayresult(pay, weekly, monthly, annual):
    print("Your weekly pay is.." + str(weekly) + "Your monthly pay is" + str(monthly) + "Your annual pay is" + str(annual))


def getRate():
    print("Enter pay rate")
    rate = float(input())

    return rate


def getHours():
    print("Enter hours worked")
    hours = float(input())

    return hours

# Main
rate = getRate()
hours = getHours()
pay = calculatePay(hours, rate)
weekly = calculateWeekly(pay)
monthly = calculateMonthly(pay)
annual = calculateAnnual(pay)
displayresult(pay, weekly, monthly, annual)