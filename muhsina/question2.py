#create a file student.txt and write your name and course intoit
'''f=open("student.txt",'x')
f.close()
f=open("student.txt",'w')
f.write("muhsina\n computer science")
f.close()

f=open("student.txt",'r')
d=f.read()
print(d)
f.close()

f=open("Sam.txt",'w')
f.write("Welcome")
f.close()

f=open("Sam.txt",'r')
d=f.read()
print(d)
f.close()'''

f=open("Sam.txt",'a')
f.write("\nPython Programming")
f.close()