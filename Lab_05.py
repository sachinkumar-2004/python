#WAP to show all the operation of calculator using function 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    return x % y

def exponentiation(x, y):
    return x ** y


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {add(num1, num2)}")
print(f"Subtraction: {subtract(num1, num2)}")
print(f"Multiplication: {multiply(num1, num2)}")
print(f"Division: {divide(num1, num2)}")
print(f"Modulus: {modulus(num1, num2)}")
print(f"Exponentiation: {exponentiation(num1, num2)}")
  

#defina a func to calculate simple and compund interst using func\

def simple_interest(p,r,t):
    si=(p*r*t)/100
    print("Simple Interest:",si)

def compound_interest(p,r,t):
    ci=p*((1+(r/100))**t)-p
    print("Compound Interest:",ci)


p=int(input("Enter the Principal Amount:"))
r=float(input("Enter the Rate of Interest:"))
t=float(input("Enter the Time(in years):"))
simple_interest(p,r,t)
compound_interest(p,r,t)


#WAP to print fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


num_terms = int(input("Enter the number of terms: "))

print("Fibonacci Series:")
fibonacci(num_terms)

#WAP to factorial of a num
def factorial(n):
    k=1
    for i in range(2,n+1):
        k*=i
    return k

n=int(input("Enter a num:"))
fact=factorial(n)
print(fact)    

#WAP to check armstrong
num = int(input("Enter a number: "))  
sum = 0  
temp = num  
while temp > 0:  
    digit = temp % 10  
    sum += digit ** len(str(num))  
    temp //= 10  

if num == sum:  
    print(f"{num} is an Armstrong number.")  
else:  
    print(f"{num} is not an Armstrong number.")  
