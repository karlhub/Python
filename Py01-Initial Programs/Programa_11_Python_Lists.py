# Lists

# List of strings
list_str=["Estela","Oscar","Carles"]
print(list_str)
list_str=('Estela','Oscar','Carles')
print(list_str)

# list of integers
list_int=[1,2,3]
print(list_int)
for i in list_int:
    print(type(i))

# Mixed lists
list_mix=["estela","Oscar",1,2,3.2]
print(list_mix)
n=0
for i in list_mix:
    print(n,list_mix[n],"-",i,type(i))
    n=n+1

# List of lists
list_str=["Estela","Oscar","Carles"]
list_int=[1,2,3]
list_lst=[list_str,list_int]
print(list_lst)

# Empty list
list_emp=[]
print(list_emp)

# Lists are mutable, but strings are not
str="Banana"
try:
    str[0]="b"
except:
    print("Strings are not mutable")
print(str)
str_cpy=str.lower()
print(str_cpy)

lst=["B","a","n","a","n","a"]
print(lst)
lst[0]="b"
print(lst)
print("Lists are mutable")

# Lists have length, like strings
list_str=["Estela","Oscar","Carles"]
list_int=[1,2,3]
list_lst=[list_str,list_int]
print("Length:",len(list_lst),"=>",list_lst)

# "Range" function
rng=input("Range:")
try:
    rng_int=int(rng)
except:
    print("Range must be an integer")
    quit()
print(range(rng_int))
lst=range(rng_int)
lst[0]=lst[:]
print(lst)
for i in range(len(lst)):
    print(i,lst[i])

# Cocatenate lists, like with strings
a=[1,2,3,4]
b=[5,6,7,8,9]
c=a+b
print("a:",a)
print("b:",b)
print("c:",c)

# Slicing lists, like with strings
l=[1,2,3,4,5,6,7,8,9]
print("list[2:4]",l[2:4])
print("list[:5]",l[:5])
print("list[1:]",l[1:])
print("list[:]",l[:])

# List methods
l=list()
print(type(l),l)
print(dir(l))

# Create an empty list and appending elements - List is muted with the method (different from strings which are not mutable and so their methods return copies of the original string)
l=list()
elem=None
while elem!="end":
    elem=input("Element to append:")
    l.append(elem)
    print(elem)
print(l)

# Is something in a list?
e=input("Element to search:")
if e in l:
    print(e,"is in",l)
elif e not in l:
    print(e,"is not in",l)

# Sort lists
l.sort()
print("List sorted",l)

# Built-in functions
l=[3,41,12,9,74,15]
print("List:",l)
print("Min:",min(l))
print("Max:",max(l))
print("Len:",len(l))
print("Sum:",sum(l))
print("Avg:",sum(l)/len(l))

# Strings and Lists - Split method
str=input("String:")
lst=str.split() # By default, delimiter parameter is space or multiple spaces
print("String:",str)
print("List:",lst)
for i in range(len(lst)):
    print(i,lst[i])

# Strings and Lists - Split method with parameter for delimiter
str=input("String:")
lst=str.split(";")
print("String:",str)
print("List:",lst)
for i in range(len(lst)):
    print(i,lst[i])

print("=> End of program")
