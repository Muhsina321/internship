# write a program to enter the numbers till the user wants and at the end it should display the sum of all the numbers entered.
sum=0
choice="y"
while choice=="y":
    num=int(input("enter the number"))
    sum+=num
    choice=input("doyou want to continue(y/n)")
    print("sum=",sum)