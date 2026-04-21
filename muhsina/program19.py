#wirte a program to read a person's first name and last name in a single input and output: a)full name b)length full name
first_name=input("enter your first and last name:")
first_name,last_name=first_name.split()
full_name=first_name+""+last_name
print("first name:",first_name)
print("last name:",last_name)
print("full name length:",len(full_name))