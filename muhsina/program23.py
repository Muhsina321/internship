#write a program to accept date input in the format"dd-mm=yyyy" using split("-"),then print day,month,and year separately.
date_input=input("enter the dd-mm-yyyy:")
date_input,month,year=date_input.split('-')
print(date_input)
print(month)
print(year)        