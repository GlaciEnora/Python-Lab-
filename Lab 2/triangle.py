#Lab 2 Ex 3

print("Input the three sides of the triangle: ")
a = int(input())
b = int(input())
c = int(input())

if a==b and b==c:
    print("The given triangle is an equilateral triangle")

elif (a != b) and (a != c) and (b != c):
    print("The given triangle is a scalene triangle")

else:
    print("The given triangle is an isoceles triangle")
