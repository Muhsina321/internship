###list
'''#write a program to find the length of a list.
my_list=[10,20,30,40,50]
length=len(my_list)
print(length)

#write a program to find the largestelement in list.
numbers=[10,25,7,89,45]
largest=max(numbers)
print(largest)

#write a program to find the smallest element in a list.
numbers=[10,25,7,89,45]
smallest=min(numbers)
print(smallest)

#write a program to calculate the sum of elements in a list.
numbers=[10,20,30,40,50]
total=sum(numbers)
print(total)

#write a program to sort a list in ascending order.
numbers=[50,10,30,20,40]
numbers.sort()
print(numbers)

#write a program to count even and odd numbers in a list.
numbers=[10,21,32,43,54,65,76]
even_count=0
odd_count=0
for num in numbers:
    if num%2==0:
       even_count+=1
    else:
        odd_count+=1
print("number of even numbers:",even_count)
print("number of odd numbers:",odd_count)

#create a new list from the existing list such that the elements in a new list are nultiples of 3.
numbers=[2,3,5,6,9,12,14,15]
multiple_of_3=[]
for num in numbers:
    if num%3==0:
        multiple_of_3.append(num)
print("multiple of 3:",multiple_of_3)

#write a list with elements entered by the user and display the list.
n=int(input("enter a number of elements:"))
my_list=[]
for i in range(n):
    element=input("enter the element:")
    my_list.append(element)
print("the list is:",my_list)'''

###tuple
'''#write a program to find the length of a tuple.
my_tuple=(10,20,30,40,50)
length=len(my_tuple)
print(length)

#write a program to count occurrences of a element in a tuple.
my_tuple=(1,2,3,2,4,2,5)
element=int(input("enter the elementto count:"))
count=0
for item in my_tuple:
    if item==element:
        count+=1
print(f'the element{element} occurs{count} times in the tuple')

#write a program to find the max and min elements in a tuple.
my_tuple=(10,25,5,40,15)
max=my_tuple[0]
min=my_tuple[0]
for num in my_tuple:
    if num>max:
        max=num
    if num<min:
        min=num
print(max)
print(min)

#write a program to convert a list into a tuple.
n=int(input("enter thenumbers of elements in the list:"))
user_list=[]
for i in range(n):
    element=input(f'enter element{i+1}:')
    user_list.append(element)
user_tuple=tuple(user_list)
print("list entered by the user:",user_list)
print("converted tuple:",user_tuple)

#write a program to access elements of a tuple using indexing.
my_tuple=(10,20,30,40,50)
print("first element:",my_tuple[0])
print("second element:",my_tuple[1])
print("last element:",my_tuple[-1])
print("elements from index 1 to 3:",my_tuple[1:4])

#write a program to concatenate two tuples.
tuple_1=(1,2,3,4,5)
tuple_2=(6,7,8,9,10)
tuple_3=tuple_1+tuple_2
print(tuple_3)'''

###packing
'''my_tuple=10,20,30,40,50
print("packed tuple:",my_tuple)'''

###upacking
'''my_tuple=(10,20,30,40,50)
a,b,c,d,e=my_tuple
print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)
print("e=",e)'''

###dictionary
'''#how do you add a new key-value pair to a dictionary.
my_dict={'name':'muhsina','age':20}
my_dict['city']='new york'
print(my_dict)

#how do you update a value in a dictionary.
my_dict={'name':'muhsina','age':20}
my_dict['age']=23
print(my_dict)

#how do you delete an element from dicitionary.
my_dict={'name':'muhsina','age':20,'city':'new york'}
del my_dict['age']
print(my_dict)

#display all students name.
students={}
python={'muhsina':90,'ameena':95,'n.nisha':89}
print(python)

###avg
(avg=sum(students()//len students))'''