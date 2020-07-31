# Lists and Files

# Processing words of each line of the file
fhand=open("mbox-short.txt","r")
for line in fhand:
    str=line.rstrip() # Eliminate newline ("\n") and right spaces
    if not str.startswith("From "):
        continue
    lst_words=str.split() # Split line into words and put them in a List
    print(lst_words[2]) # Print the third word of the line: day of the week when the mail was sent
    email=lst_words[1] # Get the second word of the line: email address
    pieces=email.split("@")
    print(pieces[1]) # Print the host part of the email address

print("=> End of program")
