#List
a=[1,True,105,-7,2+5j,507]
a.insert(2,"I")
print(a[-3:-6:-1])

print(a[::2])
b=a.copy()
print(b)

#q
#WAP to check which element in the list consists of char g in it
fruits=["peach","watermelon","mango","apple"]
for i in fruits:
    if("g" in i):
        print(i)

#WAP to check whether the elememnts in the list contains vowels or not and store all the elemnets that contains vowels in a list
s=[]
for i in fruits:
    for j in i:
        if (j.lower() in ["a","e","i","o","u"]):
            s+=[i]
            break


print(s)        
print(type(s))  

#Tuple

b=(1,True,105,-7,2+5j,507)
print(b[-1::-2])
b=list(a)
b[2]=False
a=tuple(b)
print(a)
b=list(a)
b.extend([123,True,"AVI"])
b.pop()
b.remove(False)
a=tuple(b)

print(a)


#Set
# a={1,True,105,-7,2+5j,507,105,5.06}
# print(len(a))

# b={'Ram','Elon',1,-7}
# c=a&b
#Union(|)
#Intersect(&)
#Difference(-)
#Symmetric Difference(^)


#Dictionary
dict={"Name":"Sachin","Roll":"26","Branch": "IT"}
dict["year"]=2025
print(dict.keys())
print(dict.values())
print(dict.items())
print(100*10/60)
#WAP to check whether a key already exists in dictionary or not
a=dict.keys()
k="Name"
print(k in a)
#WAP to find 2nd largest num in a list of integers
a=[1,2,7,4,0,8,45]
a.sort()
print(a[len(a)-2])
#WAp to find common element among 3 sets``````````````````
a={1,2,3}
b={2,3,4}
c={3,4,5}
print(a&b&c)
a=['Ram',1,[-5,7.0,True]]

#6 WAP that inverse the keys and value in a dict... if multiple values are there then store in a list
dic1={"a":3,"b":2,"c":3,"d":2,"e":6,"f":7}
dic2={}
for i,j in dic1.items():
    if j in dic2:
        dic2[j]+=[i]
    else:
        dic2[j]=[i]
print(dic2)     

#7
list_a=[1,2,56,78,1,56,90,33,78]
set_1=set(list_a)
print("List:",list_a)
set_1={1,2,56,78,1,56,90,33,78}
print("Set", set_1)
if(list_a==list(set_1)):
    print("Duplicate elements present in a set")
else:
    print("Duplicate elements are not present in a set")

#8
def is_prime(n):
    if(n>=2):
        c=0
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                c+=1 
        return (c==0)
    else:
        return False    

list_a=[34,23,67,78,12,90,100]
new_list=[]

for i in range(len(list_a)):
    if is_prime(i):
        print(i,end=" ")
        new_list.append(list_a[i])
print("\n",new_list)  

#9
list_a=["Struti","Arushi","Salman","Henry","Elon"]
print(f"Original List: {list_a}")
list_a.remove("Arushi")
list_a.extend(["Rakesh","Divya"])
print(f"Length of new list: {len(list_a)}")
print(f"Position of Salman: {list_a.index("Salman")+1}")
list_a.insert(2,"Avilash")
print(f"New List: {list_a}")