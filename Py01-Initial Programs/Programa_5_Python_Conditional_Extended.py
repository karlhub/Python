# Basic program in Python - Conditional Extended
stringx=input("x:")
x=int(stringx)
print(x)

# Multi-way - Elif
if x<2:
    print("Smaller than 2")
elif x<10:
    print("Smaller than 10")
elif x<20:
    print("Smaller than 20")
else: # Optional - Else
    print("Bigger than or equal to 20")
print ("=> End Conditional Multi-way Code")

# Nested Conditional
stringx=input("x:")
stringy=input("y:")
x=int(stringx)
y=int(stringy)

if x<2:
    if y<2:
        print("x and y are smaller than 2")
    else:
        print("x is smaller than 2, but y is not")
else:
    if y<2:
        print("y is smaller than 2, but x is not")
    else:
        print("x and y are bigger than or equal to 2")
print ("=> End Nested Conditional Code")
