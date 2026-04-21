# write a program that asks the user to enter numbers continuously.
total=0
while True:
    num=int(input("enter the number"))
    if num<0:
        break
    else:
        total+=num
        print("total sum:",total)