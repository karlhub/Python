# Basic program in Python - Repeated Code - Loops and Iterations

# Basic program in Python - Repeated Code
x=5
while x>0:
    print(x)
    x=x-1
print("=> End Loop or Repeated Code")
print(x)

# Breaking out of a Loop
while True:
    line=input(">")
    if line=="done":
        break
    print(line)
print("Done!")
print(line)

# Finishing an iteration with Continue
while True:
    line=input(">")
    if line[0]=="#":
        continue
    if line=="done":
        break
    print(line)
print("Done!")

# A simple definite loop - For
for i in [5,4,3,2,1]:
    print(i)
print("=> End of definite loop")

for i in (5,4,3,2,1):
    print(i)
print("=> End of definite loop")

for i in "hello":
    print(i)
print("=> End of definite loop")

friends=("Oscar","Estela","Carles")
for friend in friends:
    print("hello",friend)
print("=> End of definite loop")

# Looping through a set

print("Before")
for thing in (3,41,12,9,74,15):
    print(thing)
    print("After")

# What is the largest number?
print("Before")
largest_so_far=0
for the_num in (3,41,12,9,74,15):
    if the_num>largest_so_far:
        largest_so_far=the_num
    print(largest_so_far,the_num)
print("After")
print("Largest number is:",largest_so_far)

# Counting in a Loop
zork=0
print("Before:",zork)
for thing in (3,41,12,9,74,15):
    zork=zork+1
    print(zork,thing)
print("After",zork)

# Summing in a Loop
zork=0
print("Before:",zork)
for thing in (3,41,12,9,74,15):
    zork=zork+thing
    print(zork,thing)
print("After",zork)

# Finding the average in a Loop
count=0
sum=0
print("Before:",count,sum)
for value in (3,41,12,9,74,15):
    count=count+1
    sum=sum+value
    avg_so_far=sum/count
    print(avg_so_far,count,sum,value)
print("After",avg_so_far)

# Filtering in a Loop
print("Before")
for value in (3,41,12,9,74,15):
    if value>20:
        print("Large number:",value)
print("After")

#Search using a boolean vriable
found=False
print("Before:",found)
for value in (3,41,12,9,74,15):
    if value==9:
        found=True
    print(found,value)
print("After:",found)

# What is the smallest number? - None Type, Operators "IS" and "IS NOT"
print("Before")
smallest_so_far=None
for the_num in (3,41,12,9,74,15):
    if the_num<smallest_so_far or smallest_so_far is None:
        smallest_so_far=the_num
    print(smallest_so_far,the_num)
print("After")
print("Smallest number is:",smallest_so_far)
