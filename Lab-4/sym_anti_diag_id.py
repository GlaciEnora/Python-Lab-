def sym(arg):
    k = len(arg)
    flag = True
    for i in range(k):
        for j in range(k):
            if arg[i][j] != arg[j][i]:
                   flag = False
    if flag == True:
        print("The given array is a symmetric array")
    else:
        print("The given array is not a symmetric array")

def anti_sym(arg):
    k = len(arg)
    flag = True
    for i in range(k):
        for j in range(k):
            if arg[i][j] != -arg[j][i]:
                flag = False
    if flag == True:
        print("The given array is a skew-symmetric array")
    else:
        print("The given array is not a skew-symmetric array")

def diag(arg):
    k = len(arg)
    flag = True
    for i in range(k):
        for j in range(k):
            if arg[i][j] != 0 and i!=j:
                flag = False

    if flag == True:
        print("The given array is a diagonal array")
    else:
        print("The given array is not a diagonal array")
        
def iden(arg):
    k = len(arg)
    flag = True
    for i in range(k):
        if arg[i][i] != 1:
            flag = False
        for j in range(k):
            if arg[i][j] != 0 and i!=j:
                flag = False

    if flag == True:
        print("The given array is an identity array")
    else:
        print("The given array is not an identity array")
        
m = int(input("Enter the number of rows/columns: "))

lis = []
for i in range(m):
    row = []
    for j in range(m):
        row.append(int(input("Enter: ")))
    lis.append(row)
print(lis)
sym(lis)
anti_sym(lis)
diag(lis)
iden(lis)
