# write a program to find product of the digits of a given number.
num=input("enter number")
product=1
for d in num:
    product*= int(d)
print(product)