from stack2 import rev

def push(arg, x):
    arg += (x,)
    return arg

def pop(arg):
    arg = arg[:-1]
    return arg

def isempty(arg):
    return not bool(len(arg))

tup = ()
n = int(input("Enter the length of the tuple: "))
for i in range(n):
    tup += (input("Enter the element: "),)
print(tup)
tup = push(tup, "One")
print(tup)
tup = pop(tup)
print(tup)
print(isempty(tup))
print(rev(tup))