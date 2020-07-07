#call the file .txt with the command open
file = open("text.txt","r")
#a bucle for for read and print the lines
for line in file:
print line,
#To close the file
file.close()

