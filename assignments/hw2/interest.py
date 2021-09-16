"""
Name: Joanna Godawa
file: interest.py

Calculates monthly interest on a credit card account based on user input, outputs the final value.

Certificate of Authenticity:
I certify that this assignment is my own work."""


def main():
    annual_interest = round(eval(
        input("Please enter the annual interest rate: ")), 2)
    billing_cycle_days = round(eval(
        input("Please enter the number of days in the billing cycle: ")), 2)
    previous_net_balance = round(eval(
        input("Please indicate your previous net account balance: ")), 2)
    payment_amt = round(eval(
        input("How much money was paid this month?: ")), 2)
    payment_date = round(eval(
        input("What day of the billing cycle was this payment made? ")), 2)

    temp1 = previous_net_balance * billing_cycle_days
    temp2 = payment_amt * (billing_cycle_days - payment_date)
    temp3 = temp1 - temp2
    avg_daily_balance = round((temp3 / billing_cycle_days), 2)
    monthly_interest = round((avg_daily_balance * ((annual_interest / 12)*.01)), 2)

    print(monthly_interest)


if __name__ == "__main__":
    main()
