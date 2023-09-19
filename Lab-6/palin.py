def palin(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return palin(string[1:-1])
    else:
        return False
    
def palinlis(arg):
    boolis = []
    for word in arg:
        boolis.append(palin(word))
    return boolis

n = int(input("Enter the number of words: "))
arg = []
for i in range(n):
    arg.append(input("Enter the string to check: "))
print(palinlis(arg))