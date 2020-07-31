# Basic program in Python - Tuples - We often use tuples in conjunction with dictionaries to accomplish multi-step tasks like sorting or looping through all of the data in a dictionary.

# Tuples are used with "(", while lists are used with"[".
tp=('hola','adios','ayer')
print("Tuple:",tp)
print("Tuple[1]:",tp[1])
print("Max:",max(tp))

for i in tp:
    print("String:",i)

# Tuples are unmutable, like strings (while lists are mutable). This is because they are stored in memory in an optimized manner.
st="hola"
print(st)
try:
    st[1]="a"
except:
    print("Strings are not mutable")
print(st)

ls=[1,2,3]
print(ls)
try:
    ls[1]=4
except:
    print("Lists are mutable")
print(ls)

tp=(1,2,3)
print(tp)
try:
    tp[1]=4
except:
    print("Tuples are not mutable")
print(tp)

# Things not to do with tuples
tp=(1,3,2)
print(tp)

try:
    tp.sort()
except:
    print("Tuples can not be sorted")

try:
    tp.append(5)
except:
    print("Tuples can not be appended")

try:
    tp.reverse()
except:
    print("Tuples can not be reversed")

# Methods of a tuple (subset of methods of a list)
tp=(1,2,3)
print(type(tp))
print(dir(tp))

# Methods index and count
tp=input("Tuple:")
print(type(tp),tp) # Input is always a string, even if the format captured is tuple like

tp=(10,20,30,40,10,60)
print("Tuple:",tp,type(tp))
v=int(input("Value:"))
try:
    print("Index:",tp.index(v),"Value:",v)
except:
    print("Value does not exist:",v)
print("Tuple count:",v,tp.count(v))

# Tuples allow multiple assignments in just 1 line of code
(x,y)=(5,"hola")
print("(x,y)=",x,",",y)

# Tuples and Dictionaries
d=dict()
d["hola"]=2
d["adios"]=4
print("Dictionary:",d)

for k,v in d.items():
    print(k,v)

tups=d.items()
print(type(tups),"List of tuples:",tups)

# Tuples are comparable
tp1=(1,"aa",3,4)
tp2=(1,"ab",3,4)
if tp1<tp2:
    print(tp1,"<",tp2)
elif tp1>tp2:
    print(tp1,">",tp2)
else:
    print(tp1,"=",tp2)

# Sorting lists of tuples to get a sorted version of a dictionary
d={"d":3,"b":16,"a":5,"c":4}
print(type(d),d)
print("Dictionary items:",d.items())
lst=sorted(d.items())
print("Sorted:",type(lst),lst)
print("Sorted:",type(d),d)
print("Sorted Dc. items:",d.items())

for k,v in sorted(d.items()):
    print(k,v)

# Sort by values instead of keys
d={"d":3,"b":16,"a":5,"c":4}
print("Dictionary items:",d.items())
lst=list()
for k,v in d.items():
    lst.append((v,k))
print("List Value-Key:",lst)
lst_ord=sorted(lst,reverse=True)
print("Sort Value-Key:",lst_ord)

print ("=> End of program")
