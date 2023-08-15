from math import sqrt

x1 = float(input("Enter the x-coordinates of the first point: "))
y1 = float(input("Enter the y-coordinates of the first point: "))
x2 = float(input("Enter the x-coordinates of the second point: "))
y2 = float(input("Enter the y-coordinates of the second point: "))

print("Distance between the two points: ", sqrt((x2-x1)**2 + (y2-y1)**2))
