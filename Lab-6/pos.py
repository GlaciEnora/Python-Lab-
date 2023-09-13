def pos(num):
    if num == 0:
        return 0
    else:
        return 1+pos(num//10)


n = int(input("Enter the number: "))
print("The number of digits in the given number is: ", pos(n))
