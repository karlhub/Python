# Basic program in Python - Story: Top 10 most common words in a file

# Get the name of the file and open it
namef=input("Enter file: ")
handle=open(namef,'r')

# Count word frequency
counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

# Create a list to store the tuples (key,value) of the dictionary
lst=list()
for k,v in counts.items():
    lst.append((v,k))

# Sort reverse the list
lst=sorted(lst,reverse=True)
for v,k in lst[:10]:
    print(k,v)

# Another equivalent way of doing 2 paragraphs above - List Comprehension
print(sorted([(v,k) for k,v in counts.items()],reverse=True)[:10])

print ("=> End Story: Top 10 most common words in a file")
