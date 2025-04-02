# Program to input and display personal and academic details

name = input("Enter your name: ")
reg_no = input("Enter your registration number: ")
university = input("Enter your university name: ")
branch = input("Enter your branch: ")
section = input("Enter your section: ")

print("\nPersonal and Academic Details:")
print("Name         :", name)
print("Reg. No.     :", reg_no)
print("University   :", university)
print("Branch       :", branch)
print("Section      :", section)

# Program to demonstrate type casting in Python

int_var = int(input("Enter an integer: "))  # Input as integer
float_var = float(input("Enter a float: "))  # Input as float
str_var = input("Enter a string: ")  # Input as string
bool_var = bool(int(input("Enter 1 for True or 0 for False: ")))  # Input as boolean

int_to_float = float(int_var)
int_to_str = str(int_var)
int_to_bool = bool(int_var)

float_to_int = int(float_var)
float_to_str = str(float_var)
float_to_bool = bool(float_var)

bool_to_int = int(bool_var)
bool_to_str = str(bool_var)

print("\nType Casting Results:")
print(f"Integer to Float: {int_to_float}, String: '{int_to_str}', Boolean: {int_to_bool}")
print(f"Float to Integer: {float_to_int}, String: '{float_to_str}', Boolean: {float_to_bool}")
print(f"Boolean to Integer: {bool_to_int}, String: '{bool_to_str}'")

# Program to calculate the average of three numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

average = (num1 + num2 + num3) / 3
print(f"The average of {num1}, {num2}, and {num3} is: {average}")

#que1
# Full Pyramid Pattern
rows = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)


#que2
# Diamond Pattern
rows = int(input("Enter the number of rows for the diamond (half): "))

# Top half of the diamond
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)

# Bottom half of the diamond
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    print("* " * i)


#que3
# Half Diamond Pattern
rows = int(input("Enter the number of rows for the half diamond: "))
for i in range(1, rows + 1):
    print("* " * i)
for i in range(rows - 1, 0, -1):
    print("* " * i)



#que4
# Flipped Half Hourglass Pattern
rows = int(input("Enter the number of rows for the flipped half hourglass: "))
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)

for i in range(2, rows + 1):
    print(" " * (rows - i) + "* " * i)



#que5
# Flipped Half Diamond Pattern
rows = int(input("Enter the number of rows for the flipped half diamond: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)
