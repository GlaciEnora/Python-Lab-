arg = []
name = input("Enter the name of the file: ")
file = open(name, 'r')
s = ""
while True:
    i = file.read(1)
    if not i:
        break
    else:
        if i == '\n':
            arg.append(s)
            s = ""
        elif i == '':
            pass
        else:
            s += i
print(arg)
        
