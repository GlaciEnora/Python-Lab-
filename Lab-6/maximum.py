def maxi(arg, max=-1000000):
    if len(arg) == 0: return max
    if arg[0] > max:
        return maxi(arg[1:], arg[0])
    else:
        return maxi(arg[1:], max)

lis = [1, 5, 2, 9, 4]
print(maxi(lis))