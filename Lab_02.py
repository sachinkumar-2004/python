#Write the syntax of conditional statement
#WAP to check whether a citizen is senior citizen or not?
age=int(input("Enter the age:"))
if(age>60):
    print("Senior Citizen")
elif(age>18):
    print("Adult Citizen")
else:
    print("Not a Senior Citizen")          

#WAP to check whether variable container string or complex datatype
a=5+9j
if(type(a)==complex):
    print("Complex")
elif(type(a)==str):
    print("String")
else:
    print("None")   

#WAP using logical operator to show that if cgpa more than 9 and attendace more than 90%,the student qualify to IIT

cgpa=float(input("Enter the CGPA:"))
att=float(input("Enter the Attendance(in percent):"))
if(cgpa>9 and att>90):
    print("Qualified to IIT")
elif(cgpa>9 or att>90):
    print("Qualified to NIT")  
elif(not att>75 or not cgpa>6):
    print("YEAR BACK")
else:
    print("Welcome to VSSUT")

#WAP using nested if else to show whether the roll-no belongs to CS if true then show that he got grade O
roll=int(input("Enter the Roll-no:"))
cgpa=float(input("Enter the Cgpa(0-10):"))
if(roll>230 and roll<300):
    if(cgpa>9):
        print("Belongs to CS with O grade")
    else:
        print("Welcome to CS with low grade ")
else:
    if(cgpa>9):
        print("Congo for O grade")
    else:
        print("Invalid topper with non-CS bg")