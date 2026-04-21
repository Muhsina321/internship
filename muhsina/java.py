'''###append
f=open("computer1.txt",'a')
f.write("computer science")
f.close()
f=open("computer1.txt",'r')
d=f.read()
print(d)
f.close()'''

'''###write()
f=open("simple1.txt",'w')
f.write("good morning\welcome")
f.close()'''

'''###create a file
f=open("simple.txt",'x')
f.close()'''

'''###read()
f=open("sample1.txt",'r')
d=f.read()
print(d)
f.close()'''

'''###using with statments
with open("filename.txt",'mode') as f1:
     statements
with open("sample1.txt",'r') as f1:
     print(f1.read())'''

with open("sample1.txt",'r') as f1:
    print(f1.read())
    f1.close()
with open("sample1.txt",'r') as f1:
    print(f1.read())
    f1.close()
  
