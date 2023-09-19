def truepalin(arg):
    lis = [None]
    if len(arg) == 0:
        return []
    if arg[0][::] == arg[0][::-1]:
        lis[0] = True
        return lis + truepalin(arg[1:])
    else:
        lis[0] = False
        return lis + truepalin(arg[1:])
    
n = int(input("Enter the number of words: "))
arg = []
for i in range(n):
    arg.append(input("Enter the string to check: "))
print(truepalin(arg))