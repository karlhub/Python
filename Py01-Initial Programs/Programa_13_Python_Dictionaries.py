# Dictionaries - Are same as associative array, HashMap, Property Bag: key + value

# Create a dictionary
dct=dict()
while True:
    key=input("Key:")
    if key=="End":
        break
    value=int(input("Value:"))
    dct[key]=value
print(dct)

# Retrieve and update a Value - Dictionaries contents are mutable
key=input("Key to retrieve:")
value=int(input("Value to add:"))
dct[key]=dct[key]+value
print(dct)

# Create a dictionary from a constant value
dct={"hola":1,"adios":52,"ayer":3}
print(dct)
dct={}
print(dct)

# Count number of occurrences of all words
dct=dict()
while True:
    key=input("Key:")
    if key=="End":
        break
    value=dct.get(key,0)+1 # "0" is the default value returned by "get" method in case "key" is not in dictionary.
    dct[key]=value
print(dct)
values=dct.values()
print(values)

# Check if a key is in the dictionary (as a reference to an unexisting key causes an error)
dct=dict()
dct={"hola":1,"adios":53}
while True:
    key=input("Key:")
    if key=="End":
        break
    if key in dct:
        print(True)
    elif key not in dct:
        print(False)

# Another way of counting number of occurrences of all words
dct=dict()
lst=list()
while True:
    wrd=input("Word:")
    if wrd==".":
        break
    lst.append(wrd)
print(lst)

for wrd in lst:
    if wrd in dct:
        dct[wrd]=dct[wrd]+1
    else:
        dct[wrd]=1
print(dct)

# Yet another way of counting number of occurrences of all words - Get method instead of If-Else
dct=dict()
lst=list()
while True:
    wrd=input("Word:")
    if wrd==".":
        break
    lst.append(wrd)
print(lst)

for wrd in lst:
    dct[wrd]=dct.get(wrd,0)+1
print(dct)

# "For" in Dictionaries
dct={"hola":1,"adios":52,"ayer":3}
print(dct)
for key in dct:
    print(key,dct[key])

# Retrieving lists of Keys and Values
dct={"hola":1,"adios":52,"ayer":3}
print("Dictionary:",dct)
print("Function list:",list(dct))
print("Method keys:",dct.keys())
print("Method values:",dct.values())
print("Method items:",dct.items()) # list of tuples

print("=> End of program")
