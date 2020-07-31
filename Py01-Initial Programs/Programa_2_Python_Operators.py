# Basic program in Python - Operators and Types
x=2
x=x+8
print("Addition: ",x,type(x))
x=x-4
print("Subtraction: ",x,type(x))
x=x*3
print("Multiplication: ",x,type(x))
x=x/9
print("Division: ",x,type(x))
x=x**4
print("Power: ",x,type(x))
x=x%5
print("Remainder: ",x,type(x))
s="hello "+"world"
print("Concatenate: ",s,type(s))
print ("=> End Operators")

# Basic program in Python - Type Conversions
print(float(99)+100)
i=42
print(i,type(i))
f=float(i)
print(f,type(f))

str1="123"
str2="abc"
int1=int(str1)
# int2=int(str2) - Error
print(str1,type(str1),int1,type(int1))
# print(str2,type(str2),int2,type(int2)) - Error

# Strings operated with numbers
str="Hello "+("Hey "*5)+"bye"
print(str)

# Operating with Booleans
a=True
b=False
print(a,"+",b,"=",a+b)
a=False
b=False
print(a,"+",b,"=",a+b)
a=True
b=True
print(a,"+",b,"=",a+b)

print("=> End of program")
