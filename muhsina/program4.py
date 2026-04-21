# Ask the user for balance and withdrawal amount.
balance=int(input("enter your balance:"))
withdraw=int(input("enter withdrawel amount:"))
if withdraw <= balance:
    print("transaction successful:")
    print("remaining balance:",balance-withdraw)
else:
    print("insufficient balance")