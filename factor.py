def isprime(n):
    for i in range(2, n//2):
        if n%i == 0:
            return False

    else:
        return True

def factors(n):
    for i in range(1, n+1):
        if n%i == 0:
            #print(i, sep=" ")
            if isprime(i):
                print(i, end=" ")


n = int(input("Enter the number to factorise: "))
print("Prime factors of %d are"%n)
factors(n)
