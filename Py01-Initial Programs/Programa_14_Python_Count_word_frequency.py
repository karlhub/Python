# Basic program in Python - Story: How to count words in a file

# Get the name of the file and open it
namef=input("Enter file: ")
handle=open(namef,'r')

# Count word frequency
counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

# Find the most common word
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword=word
        bigcount=count

# All done
print(bigword,bigcount)
print ("=> End Story: How to count words in a file")
