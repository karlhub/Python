# Basic program in Python - Store and Reuse - Functions

# Define new function called "thing"
def thing():
    print("Hello")
    print("Inside function thing")

# Call or invoke function "thing"
thing()
print("Zip")
thing()

# Call existing function "max" - Returns the biggest letter of a given string
big=max("hello world")
print("max(hello world):",big)

# Functions with arguments (parameters)
def greet(lang):
    if lang=="es":
        print("hola")
    elif lang=="fr":
        print("bonjour")
    else:
        print("hello")

l=input("Language:")
greet(l)

# Functions returning values
def smaller(x,y,z):
    sm=min(x,y,z)
    return sm

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
sma=smaller(a,b,c)
print("The smaller number is:",sma)

# Function help() to obtain help about any Function
f=input("Function for which you need help:")
print(help(f))

print("=> End of program")
