###exeption
'''#write a program to display a custom error message when an exception occurs.
num1=int(input("enter numerator:"))
num2=int(input("enter numerator:"))
result=num1/num2
print("result:",result)
except ZeroDivisionError:
      print("error:you cannot divide by zero!")
except ValueError:
       print("error:invalid input! please enter numbers only")
except Exception as e:
       print("completed")

a=10
b=7
c=a/b
Exception
try:
    a=10
    b=7
    c=a/b
except:
    print("exception")
else:
    print("invalid")
finally:
    print("completed")

#write a function calculator a,b,operater that perforamance
def calculator(a,b,operater):
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    if operater=='+':
        return(a+b)
    elif operater=='*':
        return(a*b)
    elif operater=='-':
        return(a-b)
    else:
        return(a/b)
        res=(a,b,operater)
        print(res)'''