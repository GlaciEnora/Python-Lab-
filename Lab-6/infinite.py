def somefunc(x, i=1):
    if i == 2**20:
        return 0
    return ((i**x)/i) + somefunc(x, i*2)


num = int(input("Enter the number..."))
print("Sum of the given series for upto 20 terms: ", somefunc(num))
