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


m = int(input("Enter the number of rows/columns: "))

lis = []
for i in range(m):
    row = []
    for j in range(m):
        row.append(int(input("Enter: ")))
    lis.append(row)

print(lis)
trig_sum(lis)
