#Lab2 Ex8
from math import factorial as fact

x = int(input("Enter x: "))

sin = 0
cos = 0
e = 0

for i in range(1, 100, 2):
    k = 1
    sin += k*(x**i)/fact(i)
    k*=-1

for i in range(0, 100, 2):
    k = 1
    cos += k*(x**i)/fact(i)
    k*=-1

for i in range(1, 100):
    e += (x**i)/fact(i)

print("Sine of %d is: "%x, sin, "\nCosine of %d is: "%x, cos, "\nExp of %d is: "%x, e)
