# Basic program in Python - Strings

# Looking inside strings
fruit="banana"
for letter in fruit:
    print(letter)
print("End of loop:",i)

pos=input("Position:")
try:
    print(fruit[int(pos)])
except:
    print(fruit)

# Length of an string
fruit=input("Fruit:")
l=len(fruit)
print("Length:",l)
i=0
while i<l:
    letter=fruit[i]
    print(i,letter)
    i=i+1
print("=> End of program")

# Looping and Counting
str=input("String:")
cha=input("Character to count:")
counter=0
for ch in str:
    if ch==cha:
        counter=counter+1
print("Number of",cha,":",counter)
print("=> End of program")

# Slicing Strings
str=input("String:")
a=input("Ini:")
b=input("End:")
print(str,"[",a,":",b,"]")
try:
    ai=int(a)
    bi=int(b)
    print(str[ai:bi])
except:
    print("Invalid interval")
print("string[:]",str[:])
print("string[:2]",str[:2])
print("string[3:]",str[3:])
print("=> End of program")

# Concatenate Strings
str1=input("String 1:")
str2=input("String 2:")
str_res=str1+" "+str2
print("String 1:",str1)
print("String 2:",str2)
print("String Res:",str_res)
print("=> End of program")

# Using "in" as logical Operator
str=input("String:")
substr=input("Substring to find:")
found=substr in str
print("Found?",found)
print("=> End of program")

# String comparison
str1=input("String 1:")
str2=input("String 2:")
if str1<str2:
    print(str1,"<",str2)
elif str1>str2:
    print(str1,">",str2)
else:
    print(str1,"=",str2)
print("=> End of program")

# String Library - Already built into every string. Functions are Methods

# List of all methods of the object or class "string" - "dir"
str=input("String:")
print(type(str))
print(dir(str))
print("=> End of program")

# Create a copy of the string but all letters in lowercase or in uppercase
str=input("String:")
l=str.lower()
u=str.upper()
print("Original:",str)
print("Lower   :",l)
print("Upper   :",u)
print("=> End of program")

# Find a Substring
str=input("String:")
substr=input("Substring:")
pos=str.find(substr)
print(str,substr,pos)
print("=> End of program")

# Search and Replace
str=input("String:")
fnd=input("Substring to replace:")
rpl=input("Substring final:")
str_new=str.replace(fnd,rpl)
print(str)
print(str_new)
print("=> End of program")

# Stripping Whitespace at the beggining and end of a stringx
str=input("String:")
print("Left whitespaces removed          :",str.lstrip())
print("Right whitespaces removed         :",str.rstrip())
print("Left and Right whitespaces removed:",str.strip())
print("=> End of program")

# Prefixes
str=input("String:")
substr=input("Substr:")
if str.startswith(substr):
    print(str,"starts with",substr)
else:
    print(str,"does not start with",substr)
print("=> End of program")

# Parsing and extracting
str="From nombre.apellido@gmail.com Sat Jan 5 09:14:35 2019"
print(str)
pos_ini=str.find("@")
print("Pos Ini:",pos_ini)
pos_end=str.find(" ",pos_ini)
print("Pos End:",pos_end)

substr=str[pos_ini+1:pos_end]
print(substr)
print("=> End of program")
