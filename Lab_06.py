#WAP to GCD and LCM of two given number 
import math
a=int(input("Enter 1st num:"))
b=int(input("Enter 2nd num:"))
gcd=math.gcd(a,b)
lcm=math.lcm(a,b)
print("GCD:",gcd)       
print("LCM:",lcm)

# #avg of three num using class
class MyCls:
    def nums(self):
        self.a=int(input("Enter 1st num:"))
        self.b=int(input("Enter 2nd num:"))
        self.c=int(input("Enter 3rd num:"))
    def avgof3(self):
        return (self.a+self.b+self.c)/3
ob=MyCls()
MyCls.nums()
print(ob.avgof3())

#WAP to show details about a student using class and object
class Stud:
    def details(self):
        self.id=int(input("Enter the id:"))
        self.name=(input("Enter the Name:"))
        self.branch=(input("Enter the Branch:"))
    def prntDetails(self):
        print("Id:",self.id)    
        print("Name:",self.name)    
        print("branch:",self.branch)

ob1=Stud()
ob1.details()        
ob1.prntDetails()  


#WAP to fetch details about an employee using classs and object id,name,age,salary,company)
class Emp:
    def details(self):
        self.id=int(input("Enter the id:"))
        self.name=(input("Enter the Name:"))
        self.age=int(input("Enter the Age:"))
        self.salary=int(input("Enter the Salary:"))
        self.company=(input("Enter the Comapny Name:"))
    def prntDetails(self):
        print("Id:",self.id)    
        print("Name:",self.name)    
        print("Age:",self.age)
        print("Salary:",self.salary)
        print("Company:",self.company)

ob2=Emp()
ob2.details()        
ob2.prntDetails()  


#WAP to show the details of a faculty member using class and obj(id,salary,position,year of experience,subject)
class Faculty:
    def details(self):
        self.id=int(input("Enter the id:"))
        self.name=(input("Enter the Name:"))
        self.Year=int(input("Enter the Year:"))
        self.salary=int(input("Enter the Salary:"))
        self.position=(input("Enter the Comapny Name:"))
        self.sub=(input("Enter the Subject:"))
    def prntDetails(self):
        print("Id:",self.id)    
        print("Name:",self.name)    
        print("Year:",self.Year)
        print("Salary:",self.salary)
        print("Position:",self.position)
        print("Subject:",self.sub)

ob3=Faculty()
ob3.details()        
ob3.prntDetails()  

#WAP using constructor to show the details of VSSut and also include a method that display student prformance year-wise(university id
#naac grade,no of students placed,no.of depts,no.of faculties,year of establishment)
class VSSUT:
    def __init__(self,id,grade,depts,faculty,year):
        self.id=id
        self.grade=grade
        self.depts=depts
        self.faculty=faculty
        self.year=year
    def prntDetails(self):
        print("Id:",self.id)    
        print("Grade:",self.grade)    
        print("Departments:",self.depts)
        print("Faculty:",self.faculty)
        print("Year:",self.year)
    def prfrmnce(self):
        self.year=int(input("Enter the year:"))
        self.stud_plcd=int(input("Enter the no. of student placed:"))
        self.total_stud=int(input("Enter the total no. of students:"))
        print("Performance:",round(self.stud_plcd/self.total_stud*100))    

ob4=VSSUT(1,"O",10,100,2000)
ob4.prntDetails()
ob4.prfrmnce()

#WAP to create a class reperesenting a circle,input methods to calculate its area and perimeters
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Area:",round(3.14*self.radius**2))
    def peri(self):
        print("Perimeter:",round(2*3.14*self.radius,2))   
rad=float(input("Enter Radius:"))
crcl=Circle(rad)
crcl.area()             
crcl.peri()             

#WAP to implement inheritance of the parent class university contains multiple child class of autonomous clgs
class University:
    def __init__(self, name):
        self.name = name
    
    def display_info(self):
        print(f"University Name: {self.name}")

class CollegeA(University):
    def __init__(self, name, college_name, courses):
        super().__init__(name)
        self.college_name = college_name
        self.courses = courses
    
    def display_info(self):
        super().display_info()
        print(f"Autonomous College: {self.college_name}")
        print(f"Courses Offered: {self.courses}")

class CollegeB(University):
    def __init__(self, name, college_name, departments):
        super().__init__(name)
        self.college_name = college_name
        self.departments = departments
    
    def display_info(self):
        super().display_info()
        print("Autonomous College:", self.college_name)
        print("Departments:",self.departments)

college1 = CollegeA("Utkal University", "BJB Autonomous College", ["CSE", "ECE", "MECH"])
college2 = CollegeB("Utkal University", "Ravenshaw Autonomous College", ["Science", "Commerce", "Arts"])

college1.display_info()
print("\n\n")
college2.display_info()

        

# WAP to create a class representing a shopping cart include methods for adding and removing items and calculating the total price
class Cart:
    def __init__(self):
        self.items={}
    def addItem(self,item,price,quantity):
        if item in self.items:
            self.items[item]["quantity"]+=quantity
        else:
            self.items[item]={"price":price,"quantity":quantity}
        print("Cart:",self.items)
    def removeItem(self, item, quantity):
        if item in self.items:
            if self.items[item]['quantity'] > quantity:
                self.items[item]['quantity'] -= quantity
                print("Cart:",self.items)
            else:
                del self.items[item]
                print("Cart:",self.items)
        else:
            print(f"{item} is not in the cart.") 

    def TotalAmount(self):
        total=0
        for item in self.items.values():
            total += item['price'] * item['quantity'] 
        return total
    
    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Shopping Cart:")
            for item, details in self.items.items():
                print(f"{item}: {details['quantity']} x {details['price']} each")
            print(f"Total Price: {self.TotalAmount():.2f}")


cart = Cart()
cart.addItem("Laptop", 1000, 1)
cart.addItem("Mouse", 50, 2)

cart.removeItem("Mouse", 1)
cart.display_cart()
print(f"Total Price: {cart.TotalAmount():.2f}")           