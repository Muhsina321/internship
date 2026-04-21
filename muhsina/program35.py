def calculate_bill(amt):
    amt=int(input("enter the price amt "))
    tax_amt=(amt*5)/100
    total_bill=amt+tax_amt
    return total_bill
total=calculate_bill('total_bill')
print(f"the total_bill is:{total}")