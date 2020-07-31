# File Processing - mbox-short.txt

# The "newline" character: "\n"
str="Hello\nWorld"
str
print(str)
print(len(str))

# Opening a File in reading mode ("r"). In case of writing it should be "w".
f_handle=open("mbox-short.txt","r")
print(f_handle)

# Reading file - Sequence of strings ended with "\n" (i.e. sequence of lines)
count=0
for line in f_handle:
    print(line)
    count=count+1
print(count,"lines")

# Reading the whole file as a one single string
f_handle=open("mbox-short.txt","r")
filestring=f_handle.read()
print(filestring)
print(len(filestring))
print(filestring[:20])

# Searching through a file
f_handle=open("mbox-short.txt","r")
for line in f_handle:
    if line.startswith("From:"):
        print(line.rstrip())

# Using "in" to select lines
f_handle=open("mbox-short.txt","r")
for line in f_handle:
    line=line.rstrip()
    if not "@uct.ac.za" in line:
        continue
    print(line)

# Prompt for filename
fname=input("Enter the file name:")
try:
    fhand=open(fname)
except:
    print("File cannot be opened:",fname)
    quit()

str=input("Enter string to find at the beginning of the line:")
count=0
for line in fhand:
    if line.startswith(str):
        count=count+1
print("There were",count,"lines starting with",str,"in",fname)

print("=> End of program")
