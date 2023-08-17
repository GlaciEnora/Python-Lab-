def volume(rad=1, h=2):
    return 3.14*rad*h

r = int(input("Enter the radius of the cylinder: "))
h = int(input("Enter the height of the cylinder: "))

print("Without default arguments: ", volume(r,h))
print("With default arguments: ", volume())
