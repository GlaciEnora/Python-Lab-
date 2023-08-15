#Lab2 Ex6

n = int(input("Enter the number of terms: "))
psum = 0
nsum = 0
pcnt = 0
ncnt = 0
zcnt = 0
pavg = 0
navg =0

print("Start entering the numbers")

while n!=0:
    a = int(input())
    n -= 1
    if a >0:
        psum += a
        pcnt += 1

    elif a ==0:
        zcnt += 1

    else:
        nsum += a
        ncnt += 1

if pcnt != 0:
    pavg = psum / pcnt
if ncnt != 0:
    navg = nsum / ncnt

print("Number of positive integers, their sum, and average: ", pcnt, psum, pavg)
print("Number of negative integers, their sum and average: ", ncnt, nsum, navg)
print("Number of zeroes: ", zcnt)
