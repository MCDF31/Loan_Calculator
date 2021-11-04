import math
text = """What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:"""

print(text)
choice = input()
if choice == "n":
    print("Enter the loan principal:")
    principal = int(input())
    payment = int(input())
    months = math.ceil(principal / payment)
    if months == 1:
        print(f"it will take {months} month to repay the loan")
    else:
        print()
        print(f"it will take {months} months to repay the loan")
else choice == "a":
    print("Enter the loan principal")
    months = int(input())
    payment = math.ceil(principal / months)
    lastpayment = principal - (months - 1) * payment
    if payment == lastpayment:
        print()
        print(f"your monthly payment = {payment}")
    else:
        print()
        print(f"your monthly payment = {payment} and the last payment = {lastpayment}")
elif choice == "p":
    print("Enter the annuity payment:")
