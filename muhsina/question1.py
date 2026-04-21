#find max element in a list without using in a list.
'''l=[30,40,55,92,20]
max=l[0]
for i in l:
    if max<i:
        max=i
print(max)'''

#takes 10 integers from the user and stores them in a list.
'''1.the largest number
2.the smallest number
3.the average of all numbers
4.create another list containing only the even numbers from the original list and display it.'''

'''list=[1,2,3,4,5,6,7,8,9,10]
print(d)'''

'''def largest():
    for i in largest:
        if largest<i:
            largest=i
    print(largest)
l=[1,2,3,4,5,6,7,8,9,10]'''

'''list_1=[1,2,3,4,5,6,7,8,9,10]
for i in list_1:
    if i<10:
      print(i)'''

list=[]
for i in range(10):
    a=int(input("enter a number"))
    list.append(a)
print(list)

largest=max(list)
smallest=min(list)
print(largest)
print(smallest)

sum=0
for i in list:
    sum=sum+i
    avg=sum/10
print(avg)

even=[]
for i in list:
    if i%2==0:
       even.append(i)
print(even)
