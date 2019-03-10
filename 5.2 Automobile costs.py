"""JIm Weisman
prg 105
Spring2019
"""
def main():
    monthly_total = monthly()
    print("You spend $" + format(monthly_total, ",.2f") + " on your car each month")
    yearly_total = yearly(monthly_total)
    print("You spend $" + format(yearly_total, ",.2f") + " this year on your car.")


def monthly():
    loan_monthly = float(input("What is you car loan payment each month?: "))
    insurance_monthly = float(input("what is your car insurance payment each month?: "))
    gas_monthly = float(input("How much did you spend on gas each month?: "))
    maint_monthly = float(input("What is the amount you spend on maintaing your car each month?: "))
    monthly_total = loan_monthly + insurance_monthly + gas_monthly + maint_monthly
    return monthly_total


def yearly(monthly_total):
    yearly_total = monthly_total * 12
    return yearly_total


main()
