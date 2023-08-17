def gcd(a, b):
    r = min(a, b)
    while r:
        if a%r == 0 and b%r == 0:
            break
        else:
            r-=1
    return r

def ReversingANumber(n):
    rev = 0
    while n !=0:
        rev = rev*10 + n%10
        n = n // 10

    return rev

