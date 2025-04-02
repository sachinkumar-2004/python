#1
for i in range(1,11):
    print(i)
#2
a=int(input("Enter the start point:"))
b=int(input("Enter the end point:"))
for i in range(a,b+1):
    if(i%2==0):
        print(i)

#3
a=int(input("Enter the end index:"))
sum=0
for i in range(1,a):
    sum+=i
print(sum)  

#4
a=int(input("Enter the start index:"))
b=int(input("Enter the end index:"))
sum=0
for i in range(a,b+1):
    if(i%2!=0):
        sum+=i
print(sum)

#5
a=int(input("Enter the number:"))
for i in range(1,11):
    print(a*i,end=" ")

#6
c=[1,2,3,5,7,34,32,67]
for i in c:
    print(i,end=" ")

# Q10
nums=int(input("Enter a three digit number:"))
temp=nums
sum=0
while(nums>0):
    rem=nums%10
    sum+=rem**3
    nums=nums//10
if temp==sum:
    print("Armstrong number")
else:
    print("Not a armstrong number")
def display_non_prime(p,q):
    print("The non-prime numbers are:", end=" ")
    for i in range(p,q+1):
        if i < 2:
            print(i, end=" ")  
        else:
            for j in range(2,(i//2)+1):
                if i%j == 0:  
                    print(i, end=" ")
                    break  

# p = int(input("Enter the starting point: "))
# q = int(input("Enter the ending point: "))
# display_non_prime(p, q)

# #Q13
def fibonacci_upto_n(n):
    a,b = 0,1
    print("Fibonacci numbers between 0 and", n, "are:", end=" ")
    while a<=n:
        print(a, end=" ")
        a, b = b, a + b  

fibonacci_upto_n(50)

#Q14
fact=int(input("Enter the number:"))
facto=1
for i in range(1,fact+1):
    facto*=i
print("The factorial is:",facto)

#Q15
string = input("Enter a string: ")
digit_count = 0
letter_count = 0
for char in string:
    if char.isdigit():  
        digit_count += 1
    elif char.isalpha():  
        letter_count += 1
print("Number of digits:", digit_count)
print("Number of letters:", letter_count)

#q17
password = input("Enter your password: ")

length = False
upper = False
lower = False
digit = False

if len(password) >= 8:
    length = True

for char in password:
    if 'A' <= char <= 'Z':
        upper = True
    elif 'a' <= char <= 'z':
        lower = True
    elif '0' <= char <= '9':
        digit = True

if length and upper and lower and digit:
    print("Password is valid")
else:
    print("Password is invalid")



#q18

month=input("Enter a month name:")
days=0
month_list=["January","March","May","July","August","October","December"]
if(month in month_list):
    days=31
elif(month=="February"):
    year=int(input("Enter the year:"))
    if(year%400==0):
        days=29
    elif(year%100==0):
        days=28
    elif(year%4==0):
        days=29
    else:
        days=28          
else:
    days=30   
print("Total days :",days)    


