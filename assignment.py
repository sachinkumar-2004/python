# Q1: Print numbers from 1 to 10
for i in range(1, 11):
    print(i, end=" ")
print("\n")

# Q2: Print even numbers in a given range
start = int(input("Enter the starting point: "))
end = int(input("Enter the end point: "))
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")

# Q3: Find the sum of all numbers from 1 to a given number
sum = 0
num = int(input("Enter the number: "))
for i in range(1, num + 1):
    sum += i
print("Sum of all numbers:", sum)
print()

# Q4: Find the sum of all odd numbers in a given range
st = int(input("Enter the start point: "))
ed = int(input("Enter the end point: "))
summing = 0
for i in range(st, ed + 1):
    if i % 2 != 0:
        summing += i
print("Sum of odd numbers is:", summing)
print()

# Q5: Print the multiplication table of a given number
a = int(input("Enter the multiplication table number: "))
for i in range(1, 11):
    print(a * i, end=" ")
print()

# Q6: Print all numbers in a list
lst = [12, 78, 90, 67.45]
print("Numbers in the list are:")
for num in lst:
    print(num, end=" ")
print("\n")

# Q7: Count the number of digits in a given number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Total number of digits are:", count)

# Q8: Check if a string is a palindrome
def is_palindrome(string):
    return string == string[::-1]

mes = input("Enter the string: ")
if is_palindrome(mes):
    print(f'"{mes}" is a palindrome!')
else:
    print(f'"{mes}" is not a palindrome.')

# Q9: Reverse a given word
word = input("Enter a word: ")
rev_word = word[::-1]
print("Reverse Word is", rev_word)

# Q10: Check if a three-digit number is an Armstrong number
nums = int(input("Enter a three-digit number: "))
temp = nums
sum = 0
while nums > 0:
    rem = nums % 10
    sum += rem ** 3
    nums = nums // 10
if temp == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# Q11: Count even and odd numbers in a given range
m = int(input("Enter the starting point: "))
n = int(input("Enter the ending point: "))
even = 0
odd = 0
for i in range(m, n + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"No of Even numbers: {even} and Odd numbers: {odd}")

# Q12: Display non-prime numbers in a given range
def display_non_prime(p, q):
    print("The non-prime numbers are:", end=" ")
    for i in range(p, q + 1):
        if i < 2:
            print(i, end=" ")
        else:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    print(i, end=" ")
                    break

p = int(input("Enter the starting point: "))
q = int(input("Enter the ending point: "))
display_non_prime(p, q)

# Q13: Print Fibonacci numbers up to a given limit
def fibonacci_upto_n(n):
    a, b = 0, 1
    print("Fibonacci numbers between 0 and", n, "are:", end=" ")
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

fibonacci_upto_n(50)

# Q14: Calculate the factorial of a given number
fact = int(input("Enter the number: "))
facto = 1
for i in range(1, fact + 1):
    facto *= i
print("The factorial is:", facto)

# Q15: Count the number of letters and digits in a string
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

# Q16: Print numbers from 1 to a given number
inte = int(input("Enter the number: "))
for i in range(1, inte + 1):
    print(i, end=" ")
print()

# Q18: Get the number of days in a given month
def month_to_days(month):
    month = month.lower()
    if month in ['january', 'march', 'may', 'july', 'august', 'october', 'december']:
        return 31
    elif month in ['april', 'june', 'september', 'november']:
        return 30
    elif month == 'february':
        return 28
    else:
        return "Invalid month name"

month = input("Enter the month name: ")
print(f"Number of days in {month}: {month_to_days(month)}")

# Check if a string is a palindrome
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# Check if an integer is a palindrome
a = int(input("Enter a number: "))
if str(a) == str(a)[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
