from math import sqrt

print("Input the sides of a triangle")
a = int(input())
b = int(input())
c = int(input())

s = (a+b+c)/2

print("Area of the triangle = ", sqrt(s*(s-a)*(s-b)*(s-c)))
      
