# Basic program in Python - Eliminate Traceback (interpreter error) - Try and Exception
astr="hello"
try:
    istr=int(astr)
except:
    istr=-1
print("First:",istr)

astr=123
try:
    istr=int(astr)
except:
    istr=-1

print("Second:",istr)

# Exception when managing input data
rawstr=input("Enter a number:")
error=False
try:
    ival=int(rawstr)
except:
    error=True

if error:
    print("Not a number")
else:
    print("Nice work:",ival)
