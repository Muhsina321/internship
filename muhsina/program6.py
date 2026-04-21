# write a program to check weather a given number is prime or not.
num=int(input("enter a number"))
for i in range(2,num):
    if num%i==0:
        print("not a prime number")
        break
    else:
        if num>1:
            print("prime number")
        else:
            print("not a prime number") 