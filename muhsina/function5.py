# find the sum of fist n natural numbers using python(function without arguement and return function).
def display():
    n=int(input("enter the first n natural numbers"))
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print(sum)
display()