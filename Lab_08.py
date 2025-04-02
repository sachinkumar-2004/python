#WAP to return the entire statement using regular expression with valid symbolization:
#  "This is our demo lesson"
#  "This is for you"
#  "The class has some of the good minds."

import re
mes1="This is our demo lesson."
pattern = r"^This.*.$"
msg=re.search(pattern,mes1)
if msg:
    print("Matched")
else:
    print("Not Matched")    

f1=open("myfile.txt","r")
f2=open('D:\\file\myfile.txt',"r")
print(f1.readline())
f1.close()

f=open("myfile.txt","a")
f=open("myfile.txt","r")
print(f.read())

f=open("myfile.txt","w")
f.write("This is a new line""As I have deleted my prev. lines")
f.close()
f=open("myfile.txt","r")
print(f.read())

#WAP using file handling to check whether exists or not,if exists then delete it
import os
f=open("myfile.txt","r")
if os.path.exists(f):
    os.remove("myfile.txt")
else:
    print("Not Exist")


#WAP to demonstrate how to read data from a text file 
f=open("demo.txt","r")
print(f.read())
f.close()
#WAP to demonnstrate how to append content to an existing file
f=open("demo.txt","a")
print(f.write("\nhow r u"))
f.close()
f=open("demo.txt","r")
print(f.read())
f.close()
#WAP to check whether a file exists or not,if exists thn use the mthod to crta a new file
import os
f=open("demo.txt","r")
if os.path.exists(r"C:\Users\abhil\Desktop\Clg\Python\demo.txt"):
    print("exists")
    f2=open("demo1.txt","x")
    print("new file created")
else:
    print("Not exists")      
f.close()
f2.close()