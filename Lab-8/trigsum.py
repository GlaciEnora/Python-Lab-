def trig_sum(arg):
    z = 1
    upsum = 0
    downsum = 0
    for i in range(len(arg)):
        for j in range(i, len(arg)):
            upsum += arg[i][j]
        for k in range(0,z):
            downsum += arg[i][k]
        z += 1
    print("Upper triangular sum: ", upsum)
    print("Lower Triangular sum: ", downsum)

row = int(input("Enter the number of rows: "))
rowmat=[]
col = int(input("Enter the number of columns: "))
colmat=[]

try:
    if row != col:
        raise IndexError
    else:
        for i in range(row):
            for j in range(col):
                colmat.append(int(input("Enter: ")))
            rowmat.append(colmat)
        trig_sum(rowmat)
except IndexError:
    print("An error has occured")
