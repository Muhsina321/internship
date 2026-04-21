# build a simple ATM simulation.
balance=int(input("enter your balance:"))
withdraw=int(input("enter withdrawal amount:"))
if withdraw <= balance:
    balance=balance-withdraw
    print("transaction successful")
    print ("remaining balance:",balance)
else:
    print("insufficient balance")