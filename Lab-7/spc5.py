name = input("Enter the file name: ")
file = open(name, 'r')
name2 = input("Enter the file to write: ")
fout = open(name2, 'w+')
spc = ""
for each in file:
    for item in each:
        if item.isascii() and not item.isalnum() and item != '\n':
            spc += item
        if each.index(item)%5 == 0:
            #print(item, end = " ")
            fout.write(item)
print(spc)

file.close()
fout.close()
