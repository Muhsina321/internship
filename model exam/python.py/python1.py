###if and else
'''#write a program to check whether the given number is 10 or not. 
num=int(input("enter a number:"))
if num==10:
    print("the number is 10")
else:
    print("the number is not 10")

#write a program to check whether a person is eligible for voting or not.
age=int(input("enter your age:"))
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

#write a program to find the largest among two numbers.
num_1=int(input("enter first number"))
num_2=int(input("enter second number"))
if num_1>num_2:
    print("the largest number is",num_1)
else:
    print("the largest number is",num_2)

#write a program to find the sum of the factors of a given number.
num=int(input("enter a number:"))
sum=0
for i in range(1,num+1):
    if num%i==0:
        sum=sum+i
print("the sum of factors",sum)

# write a program to check whether a given number is odd or even.
num=int(input("enter a number:"))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")

#write a program to check whether a given number is completely divisible by 6 or not.
num=int(input("enter a number:"))
if num%6==0:
    print("the number is completely divisible by 6")
else:
    print("the number is not completely divisible by 6")'''
###looping
'''#write a program to display your name 10 times on the screen.
for i in range(10):
    print("muhsina")

#write a program to print number from 0 to 9.
for i in range(10):
    print(i)

#write a program to display number from 1 to 10.
for i in range(1,11):
    print(i)

#write a program to display even numbers from 10 to 30.
for i in range(10,31):
    if i%2==0:
        print(i)

#write a program to find the factors of a given number.
num=int(input("enter a number:"))
print(f'factors of {num} are')
for i in range(1,num+1):
    if num%i==0:
        print(i)

#write a program to find the sum of the factors of a given numbers.
num=int(input("enter a number"))
sum=0
for i in range(1,num+1):
    if num%i==0:
        sum=sum+i
print("sum of the factor",sum)

#write a program to check whether a given number is perfect number or not.
num=int(input("enter a number:"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
        if sum==num:
           print("perfect number")
        else:
           print("not a perfect number")

#how to format output in python.
name='muhsina'
age='20'
print(f'name is{name} age is{age}')'''
###function
'''#write a function to add two numbers(4 categories)
def add():
    num_1=int(input("enter a number:"))
    num_2=int(input("enter a number:"))
    sum=num_1+num_2
    print(sum)
add()

#write a function to find the square of a number.
def square(num):
    return num*num
num_1=int(input("enter a number"))
result=square(num_1)
print(f'the square of {num_1} is {result}')
#write a function to check whether a number is even or odd.
def even_or_odd(num):
    if num%2==0:
        print(f'the number is {num} even')
    else:
        print(f'the number is {num} odd')
num_1=int(input("enter a number:"))
even_or_odd(num_1)

#write a function to find the largest of two numbers.
def largest(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
a=int(input("enter a number:"))
b=int(input("enter a number:"))
result=largest(a,b)
print(result)'''

###string
'''#write a program to count the number of charaters is a string.
num=input("enter a charater: ")
count=len(num)
print(count)

#write a program to check whether a string is a palindrome or not.
string=input("enter a string:")
rev_string=string[::-1]
if string==rev_string:
    print("its palindrome")
else:
    print("its not palindrome")

#write a program to count the number of vowles in a string.
string=input("enter a string:")
vowels="aeiouAEIOU"
count=0
for char in string:
    if char in vowels:
        count+=1
print("number of vowles:",count)

#write a program to revese a string.
string=input("enter a string:")
rev_str=string[::-1]
print("reversed string:",rev_str)

#write a program to remove spaces from a string.
string=input("enter a string:")
result=""
for char in string:
    if char!="":
        result+=char
print(result)

#write a program to find frequency of a character in a string.
string=input("enter a string:")
char=input("enter a character to find:")
count=0
for c in string:
    if c==char:
        count+=1
print("frequency of",char,"is:",count)

#write a program to replace a word in a string.
string=input("enter a string:")
old_word=input("enter the word to replace:")
new_word=input("enter the new word:")
result=string.replace(old_word,new_word)
print("updated string:",result)''' h0hyiuhg
  hguhbpjpo4jf
\\kk.assert





ash