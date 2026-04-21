#write a program to find the largest of three numbers.
x=int(input("enter first num:"))
y=int(input("enter the second num:"))
z=int(input("enter the third num:"))
if x>y and x>z:
    print("first is large num:",x)
elif y>z:
    print("second is large num:",y)
else:
    print("third is large num:",z)
