#find the factorial of given number using function.
def factorial_1():
    n=int(input("enter a number"))
    product=1
    for i in range(1,n+1):
        product=product*i
    print(product)
factorial_1() 