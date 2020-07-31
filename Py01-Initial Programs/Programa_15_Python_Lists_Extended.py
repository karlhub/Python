# Lists - More about lists

# Lists can have negative indexes
l=list()
while True:
    elem=input("Enter list element:")
    l.append(elem)
    if elem=="End":
        break
print(l)
length=len(l)
print("Longitud:",length)

i=0
j=-1
while i<length:
    print("l[",i,"]",l[i],"---","l[",j,"]",l[j])
    i=i+1
    j=j-1

# Deleting elements of a list
lst=["a","b","c","d","e","f","g"]
print("Original List",lst)
try:
    i=int(input("Element to delete:"))
except:
    print("Index must be an integer")
    exit()
try:
    del(lst[i])
except:
    print("Out of range")
    exit()
print("Updated List:",lst)

# List variables are references to the list stored in memory, but not the list itself
x=[1,2,3,4]
y=x
print("x:",x)
print("y:",y)
y[1]=99
print("y[1]=99")
print("x:",x)
print("y:",y)

# To create a copy of the list do the following insted
x=[1,2,3]
y=list()
y=x[:]
print("x:",x)
print("y:",y)
y[1]=99
print("y[1]=99")
print("x:",x)
print("y:",y)

print("=> End of program")
